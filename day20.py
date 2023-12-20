from utils import *
from queue import Queue
from math import lcm


HIGH = True
LOW = False

class FlipFlop:

	def __init__(self, s):
		self.state = False
		s = s[1:] #Retrait du %
		self.name, tar = s.split(" -> ")
		self.targets = tar.split(", ")

	def low(self, origine):
		# Inversion du state
		self.state = not self.state
		#On renvoie high si maintenant on, donc ça revient à renvoyer le state
		return self.state

	def high(self, origine):
		return

	def toKey(self):
		return (self.name, self.state)

class Conjunction:

	def __init__(self, s):
		s = s[1:] #Retrait du #
		self.name, tar = s.split(" -> ")
		self.targets = tar.split(", ")

	def initRegister(self, ins):
		self.reg = dict()
		for i in ins:
			self.reg[i] = LOW

	def low(self, origine):
		return self.treat(origine, LOW)

	def high(self, origine):
		return self.treat(origine, HIGH)

	def treat(self, origine, level):
		self.reg[origine] = level
		res = True
		for v in self.reg.values():
			res = res and v
		if res: # all high
			return LOW
		else:
		 	return HIGH

	def toKey(self):
		listKey = reg.keys()
		listKey.sort() #Pour s'assurer qu'on reste dans le même ordre
		inner = ((k, self.reg[k]) for k in listKey)
		return (self.name, inner)

class Broadcaster:

	def __init__(self, s):
		self.name, tar = s.split(" -> ")
		self.targets = tar.split(", ")

	def low(self, origine):
		return LOW

	def high(self, origine):
		return HIGH

	def toKey(self):
		return ("broadcaster")

def day20():
	content = loadFileByLine(20, "")
	dictObjects, _ = initObjects(content)
	nbrLow, nbrHigh = 0, 0
	for i in range(1000):
		l, h = cycle(dictObjects)
		nbrLow += l
		nbrHigh += h
	print(nbrLow, nbrHigh)
	return nbrLow * nbrHigh

def initObjects(content):
	dictObjects = dict()
	listCon = []
	dictInp = dict()
	tarBroad = []
	for l in content:
		if l[0] == "%":
			o = FlipFlop(l)
		elif l[0] == "&":
			o = Conjunction(l)
			listCon.append(o)
		else:
			o = Broadcaster(l)
		dictObjects[o.name] = o
		for t in o.targets:
			if t not in dictInp:
				dictInp[t] = []
			dictInp[t].append(o.name)
	for c in listCon:
		c.initRegister(dictInp[c.name])
	return (dictObjects, dictInp)

def cycle(dictObjects):
	nbrLow = 1 #On compte celui du bouton
	nbrHigh = 0
	q = Queue()
	q.put(("broadcaster", "button", LOW))
	while not q.empty():
		tar, origine, sig = q.get()
		if tar not in dictObjects:
			continue
		o = dictObjects[tar]
		if sig:
			nextSig = o.high(origine)
		else:
			nextSig = o.low(origine)
		if nextSig is not None:
			for t in o.targets:
				q.put((t, o.name, nextSig))
				if nextSig:
					nbrHigh += 1
				else:
					nbrLow += 1

	return (nbrLow, nbrHigh)

def day20Second():
	content = loadFileByLine(20, "")
	dictObjects, dictInp = initObjects(content)
	inpRx = dictInp["rx"].pop()
	inpEnd = dictInp[inpRx]
	dictRes = dict()
	c = 0
	done = False
	while not done:
		c += 1
		res = cycleSecond(dictObjects, inpEnd)
		if len(res) > 0:
			for r in res:
				if r not in dictRes:
					dictRes[r] = c
					if len(dictRes) == len(inpEnd):
						done = True
	resLcm = 1
	for v in dictRes.values():
		resLcm = lcm(resLcm, v)

	return resLcm


def cycleSecond(dictObjects, inpEnd):
	q = Queue()
	q.put(("broadcaster", "button", LOW))
	res = []
	while not q.empty():
		tar, origine, sig = q.get()
		if tar not in dictObjects:
			continue
		o = dictObjects[tar]
		if sig:
			nextSig = o.high(origine)
		else:
			nextSig = o.low(origine)
		if nextSig is not None:
			if nextSig:
				if tar in inpEnd:
					res.append(tar)
			for t in o.targets:
				q.put((t, o.name, nextSig))

	return res

print(day20Second())