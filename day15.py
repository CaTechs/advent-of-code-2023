from utils import *

def day15():
	content = loadFile(15, "t")
	content = content.split(",")
	tot = 0
	for s in content:
		tot += hash(s)
	return tot

def hash(s):
	v = 0
	for c in s:
		v += ord(c)
		v = v * 17
		v = v % 256
	return(v)


class Boxe:
	def __init__(self, boxNumber):
		self.boxNumber = boxNumber + 1
		self.dictLens = dict()
		self.maxPos = 0

	def addLens(self, lens, foc):
		if lens in self.dictLens:
			oldL = self.dictLens[lens]
			self.dictLens[lens] = (oldL[0], foc)
		else:
			self.dictLens[lens] = (self.maxPos, foc)
			self.maxPos += 1

	def removeLens(self, lens):
		if lens in self.dictLens:
			self.dictLens.pop(lens)

	def calc(self):
		vLens = list(self.dictLens.values())
		vLens.sort()
		if (len(vLens) > 0):
			print(self.boxNumber, vLens)
		tot = 0
		for nS in rLen(vLens):
			l = vLens[nS]
			tot += self.boxNumber * (nS + 1) * l[1]
		return tot





def day15Second():
	content = loadFile(15, "")
	content = content.split(",")
	boxes = [Boxe(k) for k in range(256)]
	for s in content:
		if s[-1] == "-":
			label = s[:-1]
			boxNumber = hash(label)
			box = boxes[boxNumber]
			box.removeLens(label)
		else:
			label, f = s.split("=")
			f = int(f)
			boxNumber = hash(label)
			box = boxes[boxNumber]
			box.addLens(label, f)
	tot = 0
	for b in boxes:
		tot += b.calc()
	return tot




print(day15Second())
