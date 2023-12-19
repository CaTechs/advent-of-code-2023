from utils import *

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
dictDir = {
	"R" : RIGHT,
	"D" : DOWN,
	"U" : UP,
	"L" : LEFT
}
listDir = [RIGHT, DOWN, LEFT, UP]

def day18Shoe(suf):
	content = loadFileByLine(18, suf)
	pos = (0, 0)
	listPos = []
	listPos.append(pos)
	bord = 1
	for l in content:
		d, dis, col = l.split(" ")
		d = int(col[7])
		col = col[2:7]

		dis = int(col, 16)
		bord += dis
		d = listDir[d]

		pos = (pos[0] + dis*d[0], pos[1] + dis*d[1])
		listPos.append(pos)
	area = 0
	for i in rLen(listPos):
		x1, x2 = listPos[i], listPos[(i+1) % len(listPos)]
		area += (x1[1] + x2[1])*(x1[0] - x2[0])
	return abs(area // 2) + bord // 2 + 1
res = day18Shoe("t")
print(res)
realRes = day18Shoe("")
print(realRes)