class PlayerStat:
	def __init__(self, pid, name, pos, age, team, g, gs, mp, fgm, fga, fg, threepm, threepa, threep, twopm, twopa, twop, ftm, fta, ft, orb, drb, trb, ast, stl, blk, tov, pf, pts):
		self.pid = pid
		self.name = name
		self.age = age
		self.team = team
		self.games_played = g
		self.games_started = gs
		self.total_minutes = mp
		self.fg_made = fgm
		self.fg_attempts = fga
		self.fg_pct = fg
		self.three_made = threepm
		self.three_attempts = threepa
		self.three_pct = threep
		self.two_made = twopm
		self.two_attempts = twopa
		self.two_pct = twop
		self.ft_made = ftm
		self.ft_attempts = fta
		self.ft_pct = ft
		self.oreb = orb
		self.dreb = drb
		self.reb = trb
		self.ast = ast
		self.stl = stl
		self.block = blk
		self.to = tov
		self.fouls = pf
		self.points = pts
		
def __str__(self):
	return self.pid + self.name