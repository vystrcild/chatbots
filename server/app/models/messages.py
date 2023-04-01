from app import db
from sqlalchemy import CheckConstraint, desc
from datetime import datetime

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), CheckConstraint("type in ('system', 'human', 'ai')"), nullable=False)
    text = db.Column(db.Text, nullable=False)
    room = db.Column(db.String(255), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    is_cleared = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, user, type, text, room, datetime):
        self.user = user
        self.type = type
        self.text = text
        self.room = room
        self.datetime = datetime

    def __repr__(self):
        return f"<Message {self.id} - {self.text} by {self.type}-{self.user} in {self.room} at {self.datetime}>"

    @classmethod
    def save_message_to_db(cls, message):
        datetime_field = datetime.strptime(message["datetime"], "%Y-%m-%d %H:%M:%S.%f")
        new_message = cls(user=message["user"], type=message["type"], text=message["text"], room=message["room"], datetime=datetime_field)
        db.session.add(new_message)
        db.session.commit()

    @classmethod
    def get_last_n_messages(cls, n, room=None):
        query = cls.query
        if room:
            query = query.filter_by(room=room, is_cleared=False)

        messages = query.order_by(desc(cls.datetime)).limit(n).all()
        return messages

    @classmethod
    def clear_messages_in_room(cls, room):
        messages_to_clear = cls.query.filter_by(room=room).all()
        for message in messages_to_clear:
            message.is_cleared = True
        db.session.commit()