from flask import Flask
#from flask.ext.stormpath import StormpathManager
from flask.ext.sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)


#config
app.config.from_object(os.environ['APP_SETTINGS'])

#stormpath_manager = StormpathManager(app)
db = SQLAlchemy(app)

from app import views

