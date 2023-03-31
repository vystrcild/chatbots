import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # General Config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'blablabla'

    # Database Config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"sqlite:///{os.path.join(BASE_DIR, 'data/messages.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False