from app import db

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_name = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(255), nullable=False)

    def __init__(self, room_name, model):
        self.room_name = room_name
        self.model = model

    @classmethod
    def save_room_to_db(cls, room):
        new_room = cls(room_name=room["room_name"], model=room["model"])
        db.session.add(new_room)
        db.session.commit()