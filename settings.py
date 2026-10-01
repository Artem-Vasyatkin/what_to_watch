import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
