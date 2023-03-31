from flask_sqlalchemy import SQLAlchemy

example = {
    "id": "1",
    "user": "Me",
    "text": "Ahoj, toto je dummy zpráva",
    "room": "room1",
    "datetime": "2022-12-27 08:26:49.219717",
}


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
