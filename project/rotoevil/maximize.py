import json
import operator
from pprint import pprint

def normalize(stuff, normal):
	return stuff - normal

def findBest(normalizedlist):
	best = normalizedlist[0]
	for p in range(0, len(normalizedlist)):
		if normalizedlist[p]["overall"] > best["overall"]:
			best = normalizedlist[p]
	return best

json_data=open('players.json')
data = json.load(json_data)
pprint(data["players"][0])
json_data.close()

draftpick = data["players"][0]
playerlist = data["players"][50:]

total = {}
count = 0
for p in playerlist:
	name = p["name"]
	ppg = (draftpick["PPG"] + p["PPG"]) / 2
	apg = (draftpick["APG"] + p["APG"]) / 2
	rpg = (draftpick["RPG"] + p["RPG"]) / 2
	spg = (draftpick["SPG"] + p["SPG"]) / 2
	bpg = (draftpick["BPG"] + p["BPG"]) / 2
	threepg = (draftpick["THREEPM"] + p["THREEPM"]) / 2
	fgp = (draftpick["FGPCT"] + p["FGPCT"]) / 2
	ftp = (draftpick["FTPCT"] + p["FTPCT"]) / 2

	overall = normalize(ppg, 5.25) + normalize(apg, 5.25) + normalize(rpg, 5.25) + normalize(spg, 5.25) + normalize(bpg, 5.25) + normalize(threepg, 5.25) + normalize(fgp, 5.25) + normalize(ftp, 5.25);

	total[count] = {"name" : name, "ppg" : normalize(ppg, 5.25), "apg" : normalize(apg, 5.25), "rpg" : normalize(rpg, 5.25),"spg" : normalize(spg, 5.25), "bpg" : normalize(bpg, 5.25), "threepg" : normalize(threepg, 5.25), "fgp" : normalize(fgp, 5.25), "ftp" : normalize(ftp, 5.25), "overall" : overall}


	count = count + 1

pprint(findBest(total))

