from flask import render_template
from app import app, db
from models import RotoEvilStat
from serializers import RotoEvilStatMarshal
from flask import jsonify
from marshmallow import pprint

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/rotoevil/players', methods =['GET'])	
@app.route('/rotoevil/players.json', methods =['GET'])	
def rotoevil():
	playerList = RotoEvilStat.query.all()
	serialized = RotoEvilStatMarshal(playerList, many=True)
	
	#pprint (serialized.data)
	return jsonify( { 'players' : serialized.data } )
	#return render_template('rotoevil.html', stats=playerList)

@app.route('/playerstats')
def per36():
	#stats = RotoEvilStat.query.all()
	return render_template('per36.html', stats=stats)

