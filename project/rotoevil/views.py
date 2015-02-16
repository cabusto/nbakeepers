from flask import render_template, Blueprint
from app import app, db
from models import RotoEvilStat
from serializers import RotoEvilStatMarshal
from flask import jsonify
from marshmallow import pprint

rotoevil_blueprint = Blueprint(
    'rotoevil', __name__,
    template_folder='templates',
    static_folder='static'
)

@rotoevil_blueprint.route('/index')
@rotoevil_blueprint.route('/drafttool')
@rotoevil_blueprint.route('/drafttool.html')
def index():
	return render_template('drafttool.html')

@rotoevil_blueprint.route('/rotoevil/players', methods =['GET'])	
@rotoevil_blueprint.route('/rotoevil/players.json', methods =['GET'])	
def rotoevil():
	playerList = RotoEvilStat.query.all()
	serialized = RotoEvilStatMarshal(playerList, many=True)
	
	#pprint (serialized.data)
	return jsonify( { 'players' : serialized.data } )
	#return render_template('rotoevil.html', stats=playerList)
