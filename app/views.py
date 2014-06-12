from flask import render_template
from app import app
from CSVParser import CSVParser

@app.route('/')
def index():
	#filename = 'current_per36'
	#parser = CSVParser('app/static/data/' + filename + '.csv')
	#stats = parser.getPlayerStats()

	filename2 = 'Rotoevil_sheet'
	parser2 = CSVParser('app/static/data/' + filename2 + '.csv')
	stats2 = parser2.getRotoEvilStats()

	return render_template('index.html', player_stats = stats2)