from flask import render_template, Blueprint
from project import app


staticpages_blueprint = Blueprint(
    'staticpages', __name__,
    template_folder='templates'
)

@staticpages_blueprint.route('/')
@staticpages_blueprint.route('/welcome')
def welcome():
	return render_template('welcome.html')