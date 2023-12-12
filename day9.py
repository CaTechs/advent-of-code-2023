from utils import *

def day9():
	content = loadFileByLine(9, "")
	tot = 0
	for l in content:
		tot += calcNext(l)
	return tot

def calcNext(line):
	line = line.split(" ")
	line = [int(l) for l in line]
	history = [line]
	done = False
	while not done:
		done = True
		nextLine = [line[i + 1] - line[i] for i in range(len(line) - 1)]
		for k in nextLine:
			if not k == 0:
				# On a pas que des zéros
				done = False
		history.append(nextLine)
		line = nextLine
	delta = 0
	for l in history[::-1]:
		l.append(l[-1] + delta)
		delta = l[-1]
	return delta

def day9Second():
	content = loadFileByLine(9, "")
	tot = 0
	for l in content:
		tot += calcNextSecond(l)
	return tot

def calcNextSecond(line):
	line = line.split(" ")
	line = [int(l) for l in line]
	history = [line]
	done = False
	while not done:
		done = True
		nextLine = [line[i + 1] - line[i] for i in range(len(line) - 1)]
		for k in nextLine:
			if not k == 0:
				# On a pas que des zéros
				done = False
		history.append(nextLine)
		line = nextLine
	delta = 0
	for l in history[::-1]:
		l.insert(0, l[0] - delta)
		delta = l[0]
	return delta

print(day9Second())