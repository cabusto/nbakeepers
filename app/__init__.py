from flask import Flask
#from flask.ext.stormpath import StormpathManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.marshmallow import Marshmallow
import os


app = Flask(__name__)
bcrypt = Bcrypt(app)


#config
app.config.from_object(os.environ['APP_SETTINGS'])

#stormpath_manager = StormpathManager(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import views

