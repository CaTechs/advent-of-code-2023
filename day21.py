from utils import *
from queue import Queue

def day21():
	content = loadFileByLine(21, "")
	posS = findS(content)
	return dumbBFS(content, posS)


def dumbBFS(content, posS):
	q = Queue()
	start = (posS[0], posS[1], 0)
	seen = set()
	q.put(start)
	end = set()
	while not q.empty():
		pos = q.get()
		if pos not in seen:
			seen.add(pos)
			x,y,dis = pos
			if dis == 64:
				end.add(pos)
				continue
			else:
				nextPos = calcAdj(x, y, dis, content)
				for nP in nextPos:
					q.put(nP)
	return len(end)


def calcAdj(x, y, dis, content):
	nextPos = []
	for delta in [-1, 1]:
		cX = x + delta
		cY = y + delta
		if testInGrid(content, cX, y) and content[cX][y] != "#":
			nextPos.append((cX, y, dis + 1))
		if testInGrid(content, x, cY) and content[x][cY] != "#":
			nextPos.append((x, cY, dis + 1))
	return nextPos



def findS(content):
	for x in rLen(content):
		for y in rLen(content):
			if content[x][y] == "S":
				return (x,y)


print(day21())