from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.marshmallow import Marshmallow
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
import os


app = Flask(__name__)
bcrypt = Bcrypt(app)

#config
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)
ma = Marshmallow(app)

from project.rotoevil.views import rotoevil_blueprint
from project.home.views import home_blueprint

#register blueprints
app.register_blueprint(rotoevil_blueprint)
app.register_blueprint(home_blueprint)
