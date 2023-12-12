from utils import *
from queue import Queue


# too high
def day11():
	content = loadFileByLine(11, "")
	content = expand(content)
	gals = findGals(content)
	tot = 0
	for g in gals:
		for g2 in gals:
			tot += abs(g[0] - g2[0]) + abs(g[1] - g2[1])
	return tot//2

def findGals(content):
	gals = []
	for j in range(len(content)):
		for i in range(len(content[j])):
			c = content[j][i]
			if c == "#":
				gals.append((j,i))
	return gals


def expand(content):
	# expand column
	newGal = [[] for i in range(len(content))]
	for i in range(len(content[0])):
		empty = True
		for j in range(len(content)):
			newGal[j].append(content[j][i])
			if content[j][i] == "#":
				empty = False
		if empty:
			for j in range(len(content)):
				newGal[j].append(content[j][i])
	# expand line
	content = newGal
	newGal = []
	for j in range(len(content)):
		l = []
		empty = True
		for i in range(len(content[j])):
			c = content[j][i]
			l.append(c)
			if c == "#":
				empty = False
		newGal.append(l)
		if empty:
			newGal.append(l)
	return newGal

def day11Second():
	content = loadFileByLine(11, "")
	content = expandMil(content)
	gals = calcGalSecond(content)
	tot = 0
	for g in gals:
		for g2 in gals:
			tot += abs(g[0] - g2[0]) + abs(g[1] - g2[1])
	return tot // 2

age = 1000000
def calcGalSecond(content):
	gals = []
	countLT = 0
	for x in range(len(content)):
		lineT = True
		countCT = 0
		for y in range(len(content[x])):
			c = content[x][y]
			if not c == "X":
				lineT = False
			else:
				countCT += 1
			if c == "#":
				gals.append((x + (countLT * (age - 1)), y + (countCT * (age - 1))))
		if lineT:
			countLT += 1
	return gals

def calcAdj(x, y, dis, content):
	nextPos = []
	for dX in [-1, 0, 1]:
		for dY in [-1, 0, 1]:
			if dX == 0 and dY == 0:
				continue
			cX = x + dX
			cY = y + dY
			if cX >= 0 and cX < len(content) and cY >= 0 and cY < len(content[cX]):
				if (content[cX][cY] == "X"):
					nextPos.append((cX, cY, dis + age))
				else:
					nextPos.append((cX, cY, dis + 1))
	return nextPos

def expandMil(content):
	# expand column
	newGal = [[] for i in range(len(content))]
	for i in range(len(content[0])):
		empty = True
		for j in range(len(content)):
			if content[j][i] == "#":
				empty = False
		if not empty:
			for j in range(len(content)):
				newGal[j].append(content[j][i])
		if empty:
			for j in range(len(content)):
				newGal[j].append("X") 
	# expand line
	content = newGal
	newGal = []
	for j in range(len(content)):
		l = []
		empty = True
		for i in range(len(content[j])):
			c = content[j][i]
			l.append(c)
			if c == "#":
				empty = False
		if not empty:
			newGal.append(l)
		else:
			newGal.append(["X" for i in range(len(l))])
	return newGal

def calcBFS(g, content):
	q = Queue()
	seen = set()
	x,y = g
	q.put((x,y,0))
	tot = 0
	while not q.empty():
		x,y,dis = q.get()
		if (x,y) not in seen:
			seen.add((x,y))
			nextPos = calcAdj(x, y, dis, content)
			for p in nextPos:
				q.put(p)
			if content[x][y] == "#":
				tot += dis
	return totx

print(day11Second())
