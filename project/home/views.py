from flask import render_template, Blueprint
from project import app


home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

@home_blueprint.route('/')
@home_blueprint.route('/welcome')
def welcome():
	return render_template('welcome.html')