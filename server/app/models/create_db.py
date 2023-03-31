# TODO: Udělat to parametrizovatelné funkce
import sqlite3


# Create Messages DB
def create_messages_db():
    conn = sqlite3.connect("../data/messages.db")
    conn.close()

# Define Schema for Messages DB
def define_schema_messages():
    conn = sqlite3.connect('../data/messages.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE messages
             (id INTEGER PRIMARY KEY,
             user TEXT,
             text TEXT,
             room TEXT,
             datetime DATETIME
             )''')
    conn.commit()
    conn.close()

define_schema_messages()