def loadFile(dayNumber, end = ""):
	dayNumber = str(dayNumber)
	path = "input/day" + dayNumber + end + ".txt"
	with open(path) as f:
		res = f.read()
	return res

def loadFileByLine(dayNumber, end = ""):
	content = loadFile(dayNumber, end)
	content = content.split("\n")
	if content[-1] == "":
		content.pop()

	return content

def loadAsIntList(dayNumber, end = ""):
	return [int(x) for x in loadFileByLine(dayNumber, end)]

def prettyPrint(t):
	for l in t:
		print("".join(l))

def rLen(l):
	return range(len(l))

def __main__():
	pass