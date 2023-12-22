from utils import *
from queue import Queue

class Block():

	def __init__(self, inp):
		a,b = inp.split("~")
		self.key = inp
		self.c1 = (int(k) for k in a.split(","))
		self.c2 = (int(k) for k in b.split(","))
		self.under = set()
		self.above = set()

		x1,y1,z1 = self.c1
		x2,y2,z2 = self.c2
		self.setPos = set()
		for x in range(min(x1, x2), max(x1, x2) + 1):
			for y in range(min(y1, y2), max(y1, y2) + 1):
				self.setPos.add((x,y))
		self.height = abs(z1 - z2) + 1
		self.posZ = min(z1, z2)

	def doesInter(self, other):
		return len(self.setPos.intersection(other.setPos)) > 0

	def __eq__(self, other):
		return self.key == other.key

	def __hash__(self):
		return hash(self.key)


def day22():
	allBlocks = findAllBlocks()
	return countCanErase(allBlocks)

def findAllBlocks():
	content = loadFileByLine(22, "")
	bDropDict = dict()
	for l in content:
		b = Block(l)
		z = b.posZ
		if z not in bDropDict:
			bDropDict[z] = []
		bDropDict[z].append(b)
	listeZ = list(bDropDict.keys())
	listeZ.sort()
	dictB = dict()
	for z in listeZ:
		for b in bDropDict[z]:
			dropNextBlock(b, dictB)
	allBlocks = []
	for v in dictB.values():
		allBlocks.extend(v)
	return allBlocks

def dropNextBlock(b, dictB):
	listeZ = list(dictB.keys())
	listeZ.sort(reverse = True)
	stop = False
	for z in listeZ:
		for block in dictB[z]:
			inter = b.doesInter(block)
			if inter:
				b.under.add(block)
				block.above.add(b)
				stop = True #On arrêtera à la fin, mais on veut quand même voir si il repose pas sur deux blocks
		if stop:
			break
	if not stop:
		z = 0
	hauteur = z + b.height
	if hauteur not in dictB:
		dictB[hauteur] = []
	dictB[hauteur].append(b)

def countCanErase(allBlocks):
	tot = 0
	for b in allBlocks:
		if len(b.above) == 0:
			tot += 1
		else:
			canErase = True
			for aB in b.above:
				canErase = canErase and len(aB.under) > 1 #Si le mec au dessus à deux support, il peut en perdre un
				if not canErase:
					break
			if canErase:
				tot += 1
	return tot

def day22Second():
	allBlocks = findAllBlocks()
	res = 0
	for b in allBlocks:
		res += erase(b)
	return res

def erase(block):
	q = Queue()
	blasted = set()
	blasted.add(block)
	for b in block.above:
		q.put(b)
	while not q.empty():
		b = q.get()
		if b not in blasted:
			willFall = True
			for bel in b.under:
				if not bel in blasted:
					willFall = False
					break
			if willFall:
				blasted.add(b)
				for ab in b.above:
					q.put(ab)
	return len(blasted) - 1 # Moins un parce qu'on ne compte pas l'initial


print(day22Second())