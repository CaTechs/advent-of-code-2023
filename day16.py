from utils import *
from queue import Queue

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


class Beam():
	
	def __init__(self, x, y, heading):
		self.x = x
		self.y = y
		self.heading = heading

	def __str__(self):
		return f"{self.x} {self.y} {self.heading}"
		
	def toKey(self):
			return (self.x, self.y, self.heading)

	def tick(self):
		self.x += self.heading[0]
		self.y += self.heading[1]



def testInGrid(content, x, y):
	return x >= 0 and x < len(content) and y >= 0 and y < len(content[x])

def day16():
	content = loadFileByLine(16, "")
	return doTheLazzer(content, Beam(0, -1, RIGHT))

def day16Second():
	best = 0
	content = loadFileByLine(16, "")
	maxLine = len(content[0])
	for x in rLen(content):
		best = max(best, doTheLazzer(content, Beam(x, -1, RIGHT)))
		best = max(best, doTheLazzer(content, Beam(x, maxLine, LEFT)))
	maxCol = len(content)
	for y in rLen(content[0]):
		best = max(best, doTheLazzer(content, Beam(-1, y, DOWN)))
		best = max(best, doTheLazzer(content, Beam(maxCol, y, UP)))
	return best

def doTheLazzer(content, firstBeam):
	energ = set()
	seen = set()
	current = [firstBeam]
	while len(current) > 0:
		nextListBeam = []
		for b in current:
			b.tick() # On fait avancer le rayon
			key = b.toKey()
			if key in seen or not testInGrid(content, b.x, b.y):
				# Soit on est sorti
				# Soit on a déjà eu un rayon dans cette direction, sur cette case
				# Donc on s'arrête là
				continue
			energ.add((b.x, b.y))
			seen.add(key)

			c = content[b.x][b.y]
			if c == "/":
				# Le match case de Python 3.10 ne marche pas avec des tuples :(
				if b.heading == UP:
					b.heading = RIGHT
				elif b.heading == RIGHT:
					b.heading = UP
				elif b.heading == LEFT:
					b.heading = DOWN
				elif b.heading == DOWN:
					b.heading = LEFT
				nextListBeam.append(b)
			elif c == "\\":
				if b.heading == UP:
					b.heading = LEFT
				elif b.heading == RIGHT:
					b.heading = DOWN
				elif b.heading == LEFT:
					b.heading = UP
				elif b.heading == DOWN:
					b.heading = RIGHT
				nextListBeam.append(b)
			elif c == "|" and (b.heading == LEFT or b.heading == RIGHT):
				b.heading = UP
				newB = Beam(b.x, b.y, DOWN)
				nextListBeam.append(b)
				nextListBeam.append(newB)
			elif c == "-" and (b.heading == UP or b.heading == DOWN):
				b.heading = LEFT
				newB = Beam(b.x, b.y, RIGHT)
				nextListBeam.append(b)
				nextListBeam.append(newB)
			else:
				# Soit ., soit pointy bit de splitter
				nextListBeam.append(b)

		current = nextListBeam
	return len(energ)

print(day16Second())