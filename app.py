from flask import Flask, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.marshmallow import Marshmallow
import os


app = Flask(__name__)
bcrypt = Bcrypt(app)

#config
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)
ma = Marshmallow(app)

from project.rotoevil.views import rotoevil_blueprint
from project.staticpages.views import staticpages_blueprint

#register blueprints
app.register_blueprint(rotoevil_blueprint)
app.register_blueprint(staticpages_blueprint)

if __name__ == '__main__':
    app.run()


