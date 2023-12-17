from utils import *
from queue import PriorityQueue
import functools


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
dirs = [UP, DOWN, LEFT, RIGHT]

@functools.total_ordering
class Pos:
    def __init__(self, x, y, s, d):
        self.x = x
        self.y = y
        self.s = s
        self.d = d

    def toKey(self):
        return (self.x, self.y, self.s, self.d)

    def __eq__(self, other):
        return self.toKey() == other.toKey()

    def __lt__(self, other):
        return self.toKey() < other.toKey()


def testInGrid(content, x, y):
    return x >= 0 and x < len(content) and y >= 0 and y < len(content[x])

def day17():
    content = loadFileByLine(17, "")
    q = PriorityQueue()
    first = Pos(0, 0, 0, RIGHT)
    q.put((0, first))
    seen = set()
    tX, tY = len(content) - 1, len(content[0]) - 1
    while not q.empty():
        dis, pos = q.get()
        key = pos.toKey()

        if pos.x == tX and pos.y == tY:
            return dis

        if not key in seen:
            seen.add(key)
            for nextDir in dirs:
                straight = False
                if nextDir[0] + pos.d[0] == 0 and nextDir[1] + pos.d[1] == 0:
                    #Demi tour
                    continue
                if nextDir == pos.d:
                    straight = True
                    if pos.s == 3:
                        #On a déjà fait une ligne de 3
                        continue
                nX, nY = pos.x + nextDir[0], pos.y + nextDir[1]
                if not testInGrid(content, nX, nY):
                    # Sorti de la grille
                    continue
                nextS = pos.s + 1 if straight else 1
                nextPos = Pos(nX, nY, nextS, nextDir)
                nextDis = dis + int(content[nX][nY])
                q.put((nextDis, nextPos))

# 911 too high
def day17Second():
    content = loadFileByLine(17, "")
    q = PriorityQueue()
    first = Pos(0, 0, 0, RIGHT)
    sec = Pos(0, 0, 0, DOWN)
    q.put((0, first))
    q.put((0, sec))
    seen = set()
    tX, tY = len(content) - 1, len(content[0]) - 1
    while not q.empty():
        dis, pos = q.get()
        key = pos.toKey()

        if pos.x == tX and pos.y == tY and pos.s >= 4:
            # Relou, il faut bien faire 4 avant de pouvoir s'arrêter à la fin
            return dis

        if not key in seen:
            seen.add(key)
            for nextDir in dirs:
                straight = False
                if nextDir[0] + pos.d[0] == 0 and nextDir[1] + pos.d[1] == 0:
                    #Demi tour
                    continue
                if nextDir == pos.d:
                    straight = True
                    if pos.s == 10:
                        #On a déjà fait une ligne de 10
                        continue
                elif pos.s < 4:
                    # On a pas encore fait 4 en avant, on peut pas tourner
                    continue
                nX, nY = pos.x + nextDir[0], pos.y + nextDir[1]
                if not testInGrid(content, nX, nY):
                    # Sorti de la grille
                    continue
                nextS = pos.s + 1 if straight else 1
                nextPos = Pos(nX, nY, nextS, nextDir)
                nextDis = dis + int(content[nX][nY])
                q.put((nextDis, nextPos))

print(day17Second())