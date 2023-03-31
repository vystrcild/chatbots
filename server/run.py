from flask import request
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS

from app import create_app
from app.config import Config
from app.models.messages import Message
from app.utilities.message_utils import create_message_payload
from app.utilities.farnam.farnam import generate_farnam_reply

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
    emit("data",{'data':data,'id':request.sid},broadcast=True)

    # Save Message in DB
    Message.save_message_to_db(data)

    # Farnam Street Reply
    if data["room"] == "farnam":
        reply = generate_farnam_reply(data["text"])

        # Save Farnam Reply in DB
        Message.save_message_to_db(reply)

        emit("data", reply)


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)