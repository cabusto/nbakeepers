class RotoEvilStatCSV:
# 	def __init__(self, team, yahoo_pos, espn_pos, cbs_pos, first_name, last_name, gp, mpg, fgm, fga, fg, threepm, threepa, threep, ftm, fta, ft, ppg, orb, drb, trb, ast, to, ast_to, stl, blk, pf, dubdub, tripdub, total_min, total_fpg, total_fg, total_threepm, total_threep, total_ftm, total_fta, total_ft, total_pts, total_tor, total_orb, total_drb, total_reb, total_ast, total_to, total_stl, total_blk, total_pf,comments, name, extra): 
# #isRoto, isBCare, isH2H, isAvoid, isBBB, isSuper, isCYC, isRStart):
# 		self.team = team
# 		self.yahoo_pos = yahoo_pos
# 		self.espn_pos = espn_pos
# 		self.cbs_pos = cbs_pos
# 		self.fname = first_name
# 		self.lname = last_name
# 		self.games_played = gp
# 		self.mpg = mpg
# 		self.fg_made = fgm
# 		self.fg_attempts = fga
# 		self.fg_pct = fg
# 		self.three_made = threepm
# 		self.three_attempts = threepa
# 		self.three_pct = threep
# 		self.ft_made = ftm
# 		self.ft_attempts = fta
# 		self.ft_pct = ft
# 		self.ppg = ppg
# 		self.oreb = orb
# 		self.dreb = drb
# 		self.reb = trb
# 		self.ast = ast
# 		self.to = to
# 		self.stl = stl
# 		self.block = blk
# 		self.fouls = pf
# 		self.dubdub = dubdub
# 		self.tripdub = tripdub
# 		self.total_min = total_min
# 		self.total_fpg = total_fpg
# 		self.total_fg = total_fg 
# 		self.total_threepm = total_threepm 
# 		self.total_threep = total_threep 
# 		self.total_ftm = total_ftm 
# 		self.total_fta = total_fta 
# 		self.total_ft = total_ft 
# 		self.total_pts = total_pts 
# 		self.total_tor = total_tor 
# 		self.total_orb = total_orb 
		#self.total_drb = total_drb 
		#self.total_reb = total_reb 
		#self.total_ast = total_ast
		#self.total_to = total_to
		#self.total_stl = total_stl
		#self.total_blk = total_blk
		#self.total_pf = total_pf
		#self.comments = comments
		#self.name = extra
		#self.isRoto = isRoto
		#self.isBCare = isBCare
		#self.isH2H = isH2H
		#self.isAvoid = isAvoid
		#self.isBBB = isBBB 
		#self.isSuper = isSuper
		#self.isCYC = isCYC 
		#self.isRStart = isRStart

	def __init__(self, rank, name, yahoo, cbs, espn, auction, comment, evilrank,
	PPG,RPG,APG,THREEPM,SPG,BPG,FGPCT,FTPCT,TOPG,MPG,FGM,FGA,THREEPA,THREEPCT,FTM,FTA,OREB,DREB,
	PF,TWOPM,TWOPA,TWOPCT,DD,TD,AST_TO):
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


def __str__(self):
	return self.pid + self.name