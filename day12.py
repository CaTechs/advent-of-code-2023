from utils import *
# Me sert pour importer loadFileByLine(X, Y)
# Qui va juste lire un fichier au format dayXY.txt dans le dossier ./input
# Le X étant le jour, le Y un suffixe pour distinguer le fichier réel du fichier de test

class Univers:
	def __init__(self, currCount, seen):
		self.currCount = currCount
		self.seen = seen[:]

	def __init__(self, currCount, seen, mult):
		self.currCount = currCount
		self.seen = seen[:]
		self.mult = mult

def day12():
    content = loadFileByLine(12, "")
    tot = 0
    for l in content:
    	tot += calcLine(l, 1)
    return tot


def day12Second():
    content = loadFileByLine(12, "")
    tot = 0
    for l in content:
    	tot += calcLine(l, 5)
    return tot

def parseLine(line, time):
	line, res = line.split(" ")
	totLine, totRes = line, res
	for i in range(time - 1):
		totLine = totLine + "?" + line
		totRes = totRes + "," + res
	totRes = [int(r) for r in totRes.split(",")]
	return(totLine, totRes)

def calcLine(line, time):
	line, res = parseLine(line, time)
	fU = Univers(0, [], 1)
	listeU = [fU]
	for c in line:
		nU = []
		for u in listeU:
			if c == "?":
				# Point d'inflexion, on crée donc un nouvel univers paralèle
				newU = Univers(u.currCount, u.seen, u.mult)
				treatC(u, ".", nU, res)
				treatC(newU, "#", nU, res)
			else:
				treatC(u, c, nU, res)
		# On effondre les univers qui sont dans un état identique pour réduire le nombre à suivre
		listeU = collapseUni(nU)
	# On a fini, faut finir le count si on avait un "#" à la fin
	nU = []
	for u in listeU:
		treatC(u, ".", nU, res)
	tot = 0
	for u in nU:
		if len(u.seen) == len(res):
			tot += u.mult
	return tot

			
def treatC(u, c, nU, res):
	if c == ".":
		if u.currCount > 0:
			nbrCount = len(u.seen)
			if nbrCount < len(res) and res[nbrCount] == u.currCount:
				u.seen.append(u.currCount)
				u.currCount = 0
				nU.append(u)
			else:
				# On allait reset le count, mais on matcherait pas la prochaine cible, univers incorrect
				pass
		else:
			# Rien à faire, on est dans un creux
			nU.append(u)
	elif c == "#":
		u.currCount += 1
		if len(u.seen) < len(res) and u.currCount <= res[len(u.seen)]:
			# Le compte courant a pas dépassé la prochaine cible, on a encore une chance
			nU.append(u)

def collapseUni(listU):
	dic = dict()
	for u in listU:
		key = (u.currCount, tuple(u.seen))
		if key not in dic:
			dic[key] = []
		# Deux univers ont le même état si ils sont au même count
		# Et qu'ils ont vu les mêmes choses avant
		dic[key].append(u)
	res = []
	for v in dic.values():
		u0 = v[0]
		newU = Univers(u0.currCount, u0.seen, 0)
		for u in v:
			newU.mult += u.mult
		res.append(newU)
	return res


print(day12())
print(day12Second())