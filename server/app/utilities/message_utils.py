from datetime import datetime

def create_message_payload(message):
    return {
        "id": message.id,
        "user": message.user,
        "type": message.type,
        "text": message.text,
        "room": message.room,
        "datetime": datetime.strftime(message.datetime, "%Y-%m-%d %H:%M:%S.%f")
    }
