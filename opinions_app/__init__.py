
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = '9cfc57b8-4826-4211-a752-db77807693fd'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from . import models, forms, views, error_handlers, cli_commands  # noqa: E402, F401, E501
