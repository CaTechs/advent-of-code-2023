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
	content = loadFileByLine(18, "t")
	pos = (0, 0)
	maxX = 0
	maxY = 0
	cols = []
	starts = dict()
	ends = dict()
	for l in content:
		d, dis, col = l.split(" ")
		d = int(col[7])
		col = col[2:7]

		dis = int(col, 16)
		d = listDir[d]
		if d == DOWN or d == UP:
			if d == DOWN:
				nC = (pos[0], pos[0] + dis, pos[1])
			else:
				nC = (pos[0] - dis, pos[0], pos[1])
			cols.append(nC)
			a, b, c = nC
			if a not in starts:
				starts[a] = []
			starts[a].append(nC)
			if b not in ends:
				ends[b] = []
			ends[b].append(nC)
			
		pos = (pos[0] + dis*d[0], pos[1] + dis*d[1])
		maxX = max(pos[0], maxX)
		maxY = max(pos[1], maxY)
	activated = set()
	tot = 0
	for x in range(maxX + 1):
		if x in starts:
			activated.update(starts[x])

		loc = list(activated)
		loc.sort(key = getCol)
		for k in range(0, len(loc) - 1, 2):
			un, deux = loc[k], loc[k + 1]
			tot += deux[2] - un[2] + 1 




		if x in ends:
			for e in ends[x]:
				activated.remove(e)
	return tot



def getCol(c):
	return c[2]



print(day18Second())