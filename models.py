from app import db

class RotoEvilStat(db.Model):

	__tablename__ = "roto_evil_stats"
	id = db.Column(db.Integer, primary_key=True)
	rank = db.Column(db.Integer, nullable=False)
	name = db.Column(db.String, nullable=False)
	yahoo = db.Column(db.String, nullable=False)
	cbs = db.Column(db.String, nullable=False)
	name = db.Column(db.String, nullable=False)
	espn = db.Column(db.String, nullable=False)
	auction = db.Column(db.String, nullable=False)
	comment = db.Column(db.String, nullable=True)
	evilrank = db.Column(db.Float, nullable=False)
	PPG = db.Column(db.Float, nullable=False)
	RPG = db.Column(db.Float, nullable=False)
	APG = db.Column(db.Float, nullable=False)
	THREEPM = db.Column(db.Float, nullable=False)
	SPG = db.Column(db.Float, nullable=False)
	BPG = db.Column(db.Float, nullable=False)
	FGPCT = db.Column(db.Float, nullable=False)
	FTPCT = db.Column(db.Float, nullable=False)
	TOPG = db.Column(db.Float, nullable=False)
	MPG = db.Column(db.Float, nullable=False)
	FGM = db.Column(db.Float, nullable=False)
	FGA = db.Column(db.Float, nullable=False)
	THREEPA = db.Column(db.Float, nullable=False)
	THREEPCT = db.Column(db.Float, nullable=False)
	FTM = db.Column(db.Float, nullable=False)
	FTA = db.Column(db.Float, nullable=False)
	OREB = db.Column(db.Float, nullable=False)
	DREB = db.Column(db.Float, nullable=False)
	PF = db.Column(db.Float, nullable=False)
	TWOPM = db.Column(db.Float, nullable=False)
	TWOPA = db.Column(db.Float, nullable=False)
	TWOPCT = db.Column(db.Float, nullable=False)
	DD = db.Column(db.Float, nullable=False)
	TD = db.Column(db.Float, nullable=False)
	AST_TO = db.Column(db.Float, nullable=False)

	def __init__(self, rank, name, yahoo, cbs, espn, auction, comment, evilrank,PPG,RPG,APG,THREEPM,SPG,BPG,FGPCT,FTPCT,TOPG,MPG,FGM,FGA,THREEPA,THREEPCT,FTM,FTA,OREB,DREB,PF,TWOPM,TWOPA,TWOPCT,DD,TD,AST_TO):
		self.rank = rank
		self.name =	name
		self.yahoo = yahoo
		self.cbs = cbs
		self.espn = espn
		self.auction =  auction
		self.comment =  comment
		self.evilrank =  evilrank
		self.PPG = PPG
		self.RPG = RPG
		self.APG = APG
		self.THREEPM = THREEPM
		self.SPG = SPG
		self.BPG = BPG
		self.FGPCT = FGPCT
		self.FTPCT = FTPCT
		self.TOPG = TOPG
		self.MPG = MPG
		self.FGM = FGM
		self.FGA = FGA
		self.THREEPA = THREEPA 
		self.THREEPCT = THREEPCT
		self.FTM = FTM
		self.FTA = FTA
		self.OREB = OREB
		self.DREB = DREB
		self.PF = PF
		self.TWOPM = TWOPM 
		self.TWOPA = TWOPA
		self.TWOPCT = TWOPCT
		self.DD = DD
		self.TD = TD
		self.AST_TO = AST_TO

	#def __repr__(self):
	#	return "'player': u'{}'".format(self.name)

	