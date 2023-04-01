from flask import request
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS

from app import create_app
from app.config import Config
from app.models.messages import Message
from app.models.rooms import Room
from app.utilities.message_utils import create_message_payload
from app.utilities.farnam.farnam import generate_farnam_reply
from app.utilities.chat.chat_model import ChatModel

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
    """Event listener when client sends a message."""
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
            db_messages = Message.get_last_n_messages(5, room=data["room"])

        # Generate Chat Test Reply
        chat = ChatModel()
        chat_input = chat.prepare_chat_input(db_messages)
        print(chat_input)
        reply = chat.get_response(messages=[chat_input])

        # Save Chat Test Reply in DB
        reply_text = reply["response_text"]
        reply_object = chat.generate_chat_reply(reply_text)
        Message.save_message_to_db(reply_object)

        # Send Chat Test Reply to client
        emit("data", reply_object)


@socketio.on("clear_room")
def handle_clear_chat(room):
    """event listener when client clicks the 'clear' button"""
    Message.clear_messages_in_room(room)
    print(f"Chat input cleared for room {room}")

@socketio.on("settings")
def handle_settings(data):
    """event listener when client clicks the 'settings' button"""
    print(f"Settings: {data}")


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)