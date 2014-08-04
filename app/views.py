from flask import render_template
from app import app, db
from models import RotoEvilStat

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/rotoevil')	
def rotoevil():
	
	stats = RotoEvilStat.query.all()
	return render_template('rotoevil.html', stats=stats)

@app.route('/playerstats')
def per36():
	stats = RotoEvilStat.query.all()
	return render_template('per36.html', stats=stats)

