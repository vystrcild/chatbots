from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    room = db.Column(db.String(255), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

    def __init__(self, user, text, room, datetime):
        self.user = user
        self.text = text
        self.room = room
        self.datetime = datetime

    def __repr__(self):
        return f"<Message {self.id} - {self.text} by {self.user} in {self.room} at {self.datetime}>"

    @classmethod
    def save_message_to_db(cls, message):
        datetime_field = datetime.strptime(message["datetime"], "%Y-%m-%d %H:%M:%S.%f")
        new_message = cls(user=message["user"], text=message["text"], room=message["room"], datetime=datetime_field)
        db.session.add(new_message)
        db.session.commit()