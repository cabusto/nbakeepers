import fileinput
from app import db
from models import RotoEvilStat

db.drop_all()
db.create_all()

# import from .csv file
for line in fileinput.input('app/static/data/rotoevil_tool.csv'):
	items = line.split(',')
	r = RotoEvilStat(*items)
	db.session.add(r)
	
db.session.commit()

	
