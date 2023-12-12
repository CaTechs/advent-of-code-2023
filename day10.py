from utils import *
from queue import Queue

dictAdj = {
	"|" : [(1, 0), (-1, 0)],
	"-" : [(0, 1), (0, -1)],
	"F" : [(1, 0), (0, 1)],
	"7" : [(1, 0), (0, -1)],
	"J" : [(0, -1), (-1, 0)],
	"L" : [(0, 1), (-1, 0)],
					
}

# too high
def day10():
	content = loadFileByLine(10, "")
	seen = set()
	q = Queue()
	x, y, start = findS(content)
	q.put((x,y, 0))
	mDis = 0
	while not q.empty():
		x, y, dis = q.get()
		if (x,y) not in seen:
			mDis = max(dis, mDis)
			seen.add((x,y))
			c = content[x][y]
			if dis == 0:
				c = start
			nextPos = dictAdj[c]
			for n in nextPos:
				dX, dY = n
				q.put((x + dX, y + dY, dis + 1))


	return mDis

def findS(content):
	for i in range(len(content)):
		for j in range(len(content[i])):
			if content[i][j] == "S":
				l, r, t, b = False, False, False, False
				lc, rc, tc, bc = content[i][j - 1], content[i][j+1], content[i-1][j], content[i+1][j]
				if lc == "-" or lc == "L" or lc == "F":
					l = True
				if rc == "-" or rc == "7" or rc == "J":
					r = True
				if tc == "|" or tc == "7" or tc == "F":
					t = True
				if bc == "|" or bc == "J" or bc == "L":
					b = True
				res = [i, j]
				if t and b:
					res.append("|")
				elif t and l:
					res.append("J")
				elif t and r:
					res.append("L")
				elif l and r:
					res.append("-")
				elif l and b:
					res.append("7")
				elif r and b:
					res.append("F")
				return res

print(day10())

def day10Second():
	content = loadFileByLine(10, "")
	seen = set()
	q = Queue()
	x, y, start = findS(content)
	content = enhance(content, start)
	x, y, start = findS(content)
	loop = calcLoop((x, y, start), content)
	setRed, setBlue = set(), set()
	if start == "F" or start == "J":
		q.put((x - 1, y - 1, True)) 
		q.put((x + 1, y + 1, False)) 
	else:
		q.put((x + 1, y -1, True))
		q.put((x - 1, y + 1, False))
	redOut = False
	blueOut = False
	while not q.empty():
		x, y, isRed = q.get()
		if isRed and redOut:
			continue
		elif not isRed and blueOut:
			content
		if (x,y) not in seen:
			seen.add((x,y))
			if x % 3 == 1 and y % 3 == 1:# JE ne compte que les centres de carrs 3x3
				if isRed:
					content[x][y] = "R"
					setRed.add((x,y))
				else:
					content[x][y] = "B"
					setBlue.add((x,y))
			nextPos, exit = calcAdj(x, y, content, loop)
			if exit:
				if isRed:
					redOut = True
				else:
					blueOut = True
				continue
			else:
				for p in nextPos:
					pX, pY = p
					q.put((pX, pY, isRed))
	print(setBlue, setRed)
	prettyPrint(content)

	if redOut:
		return len(setBlue)
	else:
		return len(setRed)


def calcAdj(x,y, content, loop):
	nextPos = []
	exit = False
	for dX in [-1, 0, 1]:
		for dY in [-1, 0, 1]:
			if dX == 0 and dY == 0:
				continue
			cX = x + dX
			cY = y + dY
			if cX >= 0 and cX < len(content) and cY >= 0 and cY < len(content[cX]):
				if (cX, cY) not in loop:
					nextPos.append((cX, cY))
			else:
				# on est sorti de la grille, on est donc coté extérieur
				exit = True
	return (nextPos, exit)





def enhance(content, vS):
	res = []
	for l in content:
		h,m,b = [], [], []
		for c in l:
			start = False
			if c == "S":
				start = True
				c = vS
			e = enhanceChar(c)
			if start:
				e[1][1] = "S"
			h.extend(e[0])
			m.extend(e[1])
			b.extend(e[2])
		res.append(h)
		res.append(m)
		res.append(b)
	return res

def calcLoop(start, content):
	seen = set()
	q = Queue()
	x, y, start = start
	q.put((x,y, 0))
	mDis = 0
	while not q.empty():
		x, y, dis = q.get()
		if (x,y) not in seen:
			mDis = max(dis, mDis)
			seen.add((x,y))
			c = content[x][y]
			if dis == 0:
				c = start
			nextPos = dictAdj[c]
			for n in nextPos:
				dX, dY = n
				q.put((x + dX, y + dY, dis + 1))
	return seen

def enhanceChar(c):
	if c == ".":
		return [["x","x","x"], ["x", ".", "x"], ["x","x","x"]]
	if c == "|":
		return [["x", "|", "x"] for i in range(3)]
	if c == "-":
		return [["x","x","x"], ["-", "-", "-"], ["x","x","x"]]
	if c == "F":
		return [["x","x","x"], ["x", "F", "-"], ["x","|","x"]]
	if c == "7":
		return [["x","x","x"], ["-", "7", "x"], ["x","|","x"]]
	if c == "J":
		return [["x","|","x"], ["-", "J", "x"], ["x","x","x"]]
	if c == "L":
		return [["x","|","x"], ["x", "L", "-"], ["x","x","x"]]

def prettyPrint(t):
	for l in t:
		print("".join(l))

print(day10Second())
					