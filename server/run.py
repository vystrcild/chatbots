from flask import request
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS

from app import create_app
from app.config import Config
from app.models.messages import Message
from app.utilities.message_utils import create_message_payload
from app.utilities.farnam.farnam import generate_farnam_reply
from app.utilities.chat.chat_model import chat_model, generate_chat_reply

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

app = create_app(Config)
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app,cors_allowed_origins="*")


@socketio.on("connect")
def connected():
    """event listener when client connects to the server"""
    print(request.sid)
    print("client has connected")
    emit("connect",{"data":f"id: {request.sid} is connected"})

    # Download all messages from DB
    with app.app_context():
        messages = Message.query.all()
        result = [create_message_payload(message) for message in messages]
        emit("all_messages", result)


@socketio.on('message')
def handle_message(data):
    """event listener when client types a message"""
    print(f"data from the front end: {data}")
    emit("data",{'data':data,'id':request.sid})

    # Save Message in DB
    Message.save_message_to_db(data)

    # Farnam Street Reply
    if data["room"] == "farnam":
        reply = generate_farnam_reply(data["text"])

        # Save Farnam Reply in DB
        Message.save_message_to_db(reply)

        emit("data", reply)

    # Chat Test Reply
    if data["room"] == "chat_test":
        # Download last 5 messages from DB
        with app.app_context():
            db_messages = Message.get_last_n_messages(5)

        # Transform messages as LangChain Message objects
        chat_input = []
        # Iterate in reverse order to get the most recent messages first
        for message in reversed(db_messages):
            if message.type == "human":
                message_object = HumanMessage(content=message.text)
            elif message.type == "ai":
                message_object = AIMessage(content=message.text)
            else:
                message_object = SystemMessage(content=message.text)
            chat_input.append(message_object)

        # Generate Chat Test Reply
        reply = chat_model(messages=[chat_input])

        # Save Chat Test Reply in DB
        reply_text = reply["response_text"]
        reply_object = generate_chat_reply(reply_text)
        Message.save_message_to_db(reply_object)

        emit("data", reply_object)




if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)