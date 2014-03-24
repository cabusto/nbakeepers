from flask import render_template
from app import app
from CSVParser import CSVParser

@app.route('/')
def index():
	filename = 'current_per36'
	parser = CSVParser('app/static/data/' + filename + '.csv')
	stats = parser.getPlayerStats()
	
	return render_template('index.html',
												 player_stats = stats)