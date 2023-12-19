from utils import *
from queue import Queue

class Rule:

	def __init__(self, s):
		ifPart, self.then = s.split(":")
		self.field = ifPart[0]
		self.test = ifPart[1]
		self.target = int(ifPart[2:])

	def apply(self, part):
		v = part[self.field]
		if self.test == ">":
			return v > self.target
		else:
			return v < self.target

	def applyUni(self, uni):
		uniDeux = uni.split()
		# On rencontre un test, on divise donc notre univers en deux possibilités
		# Celle qui aurait réussi et serait envoyé ailleurs, uniDeux
		# Et celle qui doit continuer jusqu'à la prochaine règle, uni
		if self.test == ">":
			uniDeux.addAbove(self.field, self.target)
			 #+1, parce que ce sont des strictement inférieurs
			uni.addBelow(self.field, self.target + 1)
		else:
			uniDeux.addBelow(self.field, self.target)
			 #-1, parce que ce sont des strictement supérieurs
			uni.addAbove(self.field, self.target - 1)
		return uniDeux

class Workflow:

	def __init__(self, s):
		posAcc = s.find("{")
		self.name = s[:posAcc]
		w = s[posAcc + 1:-1]
		w = w.split(",")
		self.rules = []
		for r in w:
			if not ":" in r:
				self.then = r
			else:
				self.rules.append(Rule(r))

	def apply(self, part):
		for r in self.rules:
			res = r.apply(part)
			if res:
				return r.then
		# Aucune règle n'a return, on renvoie le then
		return self.then

	def applyUni(self, uni):
		newUnis = []
		for r in self.rules:
			newUni = r.applyUni(uni)
			newUni.next = r.then
			newUnis.append(newUni)
		uni.next = self.then
		return newUnis


def buildWorkflows(content):
	dictWork = dict()
	for i in rLen(content):
		l = content[i]
		if l == "":
			#Séparation workflow et pièces
			break
		work = Workflow(l)
		dictWork[work.name] = work
	return dictWork

def day19():
	content = loadFileByLine(19, "")
	dictWork = buildWorkflows(content)
	score = 0
	pStart = content.index("") + 1
	for i in range(pStart, len(content)):
		p = content[i]
		p = p[1:-1].split(",")
		part = dict()
		for v in p:
			n, val = v.split("=")
			part[n] = int(val)
		work = dictWork["in"]
		accepted = False
		while True:
			res = work.apply(part)
			if res == "A":
				accepted = True
				break
			elif res == "R":
				break
			else:
				work = dictWork[res]
		if accepted:
			for v in part.values():
				score += v

	return score

def day19Second():
	content = loadFileByLine(19, "")
	dictWork = buildWorkflows(content)
	uni = Univ()
	uni.next = "in"
	q = Queue()
	q.put(uni)
	score = 0
	while not q.empty():
		uni = q.get()
		while True:
			if uni.next == "A":
				score += uni.calcScore()
				break
			elif uni.next == "R":
				break
			newUni = dictWork[uni.next].applyUni(uni)
			for u in newUni:
				if u.next == "A":
					score += u.calcScore()
				elif u.next != "R":
					q.put(u)

	return score



class Univ:
	def __init__(self):
		self.d = dict()
		for k in "xmas":
			self.d[k] = [0, 4001]

	def split(self):
		newU = Univ()
		for k in self.d:
			newU.d[k] = self.d[k][:]
		return newU

	def addAbove(self, n, v):
		self.d[n][0] = max(self.d[n][0], v)

	def addBelow(self, n, v):
		self.d[n][1] = min(self.d[n][1], v)

	def calcScore(self):
		tot = 1
		for v in self.d.values():
			tot *= max(0, v[1] - v[0] - 1 )
		return tot


print(day19Second())
