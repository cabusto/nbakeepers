from flask import render_template, Blueprint
from project import app
from yahooapi import YahooAPI



home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

@home_blueprint.route('/')
@home_blueprint.route('/welcome')
def welcome():
    YahooAPI('keys')
    return render_template('welcome.html')