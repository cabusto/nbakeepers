import fileinput

from project import app, db
from project.models import RotoEvilStat

db.drop_all()
db.create_all()

# import from .csv file
for line in fileinput.input('project/rotoevil/static/data/rotoevil_tool.csv'):
	items = line.split(',')
	r = RotoEvilStat(*items)
	db.session.add(r)
	
db.session.commit()

	
