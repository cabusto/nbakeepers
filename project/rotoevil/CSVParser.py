import fileinput
from app import PlayerStat
from app import RotoEvilStat

class CSVParser:
	csvPath = ""

	def __init__(self, filepath):
		self.csvPath = filepath

	def setCSVPath(self, path):
		self.csvPath = path

	def setMode(self, mode):
		self.mode = mode

	def loadData(self):
		a = []
		if (not fileinput.input(self.csvPath)):
			return a

		for line in fileinput.input(self.csvPath):
			a.append(line)

		return a
	
	def getPlayerStats(self):
		data = self.loadData();
		pstats = []

		for row in data:
			items = row.split(',')
			if (items[0].isdigit()):
				p = PlayerStat(*items)
				pstats.append(p)

		return pstats
	
	def getRotoEvilStats(self):
		data = self.loadData();
		rotostats = []
		
		for row in data:
			items = row.split(',')
			r = RotoEvilStat(*items)
			rotostats.append(r)
				
		return rotostats