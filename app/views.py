from flask import render_template
from app import app, db
from models import RotoEvilStat
from flask import jsonify

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/rotoevil/players', methods =['GET'])	
def rotoevil():
	playerList = [ 
		
		{
			'rank': 1, 'name': u'Kevin Durant', 'price':	89, 'evilrank': 48.63
		},
		{
			'rank': 2, 'name': u'LeBron James', 'price': 81.00, 'evilrank': 47.63
		},
		{
			'rank': 18, 'name':	u'James Harden', 'price':	37, 'evilrank':	42.02	
		}
	]
	return jsonify( {'stats': playerList } )
	#return render_template('rotoevil.html', stats=RotoEvilStat.query.all())

@app.route('/playerstats')
def per36():
	#stats = RotoEvilStat.query.all()
	return render_template('per36.html', stats=stats)

