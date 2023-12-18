from utils import *
from queue import Queue

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
dictDir = {
	"R" : RIGHT,
	"D" : DOWN,
	"U" : UP,
	"L" : LEFT
}
listDir = [RIGHT, DOWN, LEFT, UP]

def day18():
	content = loadFileByLine(18, "")
	pos = (0, 0)
	dug = set()
	dug.add(pos)
	maxX = 0
	maxY = 0
	for l in content:
		d, dis, col = l.split(" ")
		d = dictDir[d]
		dis = int(dis)
		for i in range(dis):
			pos = (pos[0] + d[0], pos[1] + d[1])
			maxX = max(pos[0], maxX)
			maxY = max(pos[1], maxY)
			dug.add(pos)
	grid = []
	inside = fill(dug)
	for x in range(maxX + 1):
		l = []
		grid.append(l)
		for y in range(maxY + 1):
			if (x,y) in dug or (x,y) in inside:
				l.append("#")
			else:
				l.append(".")
	prettyPrint(grid)
	return len(dug.union(inside))

def fill(dug):
	seen = set()
	q = Queue()
	q.put((1,1))
	while not q.empty():
		p = q.get()
		if not p in seen:
			seen.add(p)
			for d in dictDir.values():
				nP = (p[0] + d[0], p[1] + d[1])
				if not nP in dug:
					q.put(nP)
	return seen

def day18Second():
	content = loadFileByLine(18, "")
	pos = (0, 0)
	maxX = 0
	minX = 0
	cols = []
	starts = dict()
	ends = dict()
	setPos = set()
	for l in content:
		d, dis, col = l.split(" ")
		d = int(col[7])
		col = col[2:7]

		dis = int(col, 16)
		d = listDir[d]
		if d == DOWN or d == UP:
			if d == DOWN:
				nC = (pos[0], pos[0] + dis, pos[1], True)
			else:
				nC = (pos[0] - dis, pos[0], pos[1], False)
			cols.append(nC)
			a, b, c, t = nC
			if a not in starts:
				starts[a] = []
			starts[a].append(nC)
			if b not in ends:
				ends[b] = []
			ends[b].append(nC)
			
		pos = (pos[0] + dis*d[0], pos[1] + dis*d[1])
		maxX = max(pos[0], maxX)
		minX = min(pos[0], minX)
	activated = set()
	tot = 0
	for x in range(minX, maxX + 1):

		listSE = []
		if x in starts:
			listSE.extend(starts[x])
		if x in ends:
			listSE.extend(ends[x])
			for e in ends[x]:
				activated.remove(e)
		listSE.sort(key=getCol)
		adds = []
		change = len(listSE) > 0
		for k in range(0, len(listSE) - 1, 2):
			u, s, c, t = listSE[k]
			u2, s2, c2, t2 = listSE[k + 1]
			adds.append((u, s, c, c2, t))
			if t != t2:
				# Si il sont de type différent (l'un UP et l'autre DOWN)
				# On l'ajoute deux fois, parce que au final chaque extrémité de cette limite
				# Et encore soit à l'extérieur, soit à l'intérieur
				# Donc on veut garder la parité
				adds.append(adds[-1])
			# On compte le tronçon commun ici, vu qu'il est forcemment dedans
			tot += c2 - c + 1

		if not change and totLigne > 0:
			# La ligne n'a pas changé les colonnes actives, et la précédente non plus
			# On a pas besoin de recalculer
			tot += totLigne
			continue

		loc = list(activated)
		loc.extend(adds)
		loc.sort(key = getCol)
		totLigne = 0
		for k in range(0, len(loc) - 1, 2):
			# L'intérieur, c'est d'une colonne paire à une colonne impaire
			un, deux = loc[k], loc[k + 1]
			if un == deux:
				# On est sur deux fois le même changement, on les a déjà compté, on peut les ignores
				continue
			if len(un) == 5:
				# C'est un changement, donc faut prendre le coté droit du changement
				#Plus un parce qu'on a déjà compté le tronçon commun avant, donc on compte à partir d'un plus loin
				cUn = un[3] + 1
			else:
				cUn = un[2]
			cDeux = deux[2]
			if len(deux) == 5:
				# C'est un changement, on prend le coté gauche du changement
				# Moins un, pour la même raison qu'avant, donc on recule d'un
				cDeux = cDeux - 1
			totLigne += cDeux - cUn + 1 
		tot += totLigne

		if x in starts:
			activated.update(starts[x])
		if change:
			totLigne = 0
	return tot




def getCol(c):
	return c[2]


res = day18Second()
print(res, res == 133125706867777)
