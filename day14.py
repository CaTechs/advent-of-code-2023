from utils import *

NORTH = (-1, 0)
SOUTH = (1, 0)
WEST = (0, -1)
EAST = (0, 1)

def day14():
    content = loadFileByLine(14, "")
    newGrid = []
    for l in content:
        newGrid.append(list(l))

    for x in rLen(content):
        for y in rLen(content[x]):
            if content[x][y] == "O":
                rollDir(x, y, newGrid, NORTH)
    return calcScore(newGrid)

def day14Second():
    content = loadFileByLine(14, "")
    newGrid = []
    for l in content:
        newGrid.append(list(l))

    dictGrid = dict()
    dictGrid[toKey(newGrid)] = 0
    grids = [newGrid]
    for c in range(1000000000):
        newGrid = partCycle(newGrid, NORTH)
        newGrid = partCycle(newGrid, WEST)
        newGrid = partCycle(newGrid, SOUTH)
        newGrid = partCycle(newGrid, EAST)
        key = toKey(newGrid)
        if key in dictGrid:
            #On a un cycle, on prend le match qui aurait correspondu
            racineCycle = dictGrid[key]
            break
        else:
            dictGrid[key] = c + 1
            grids.append(newGrid)
    #Le cycle va donc de la racine jusqu'au dernier élément ajouté, y'a quelque parasites au début
    tailleCycle = len(dictGrid) - racineCycle
    posDansCycle = (1000000000 - racineCycle) # On skip ceux du début
    posDansCycle = posDansCycle % tailleCycle # Modulo la taille pour connaitre la position correspondante
    # Il faut skip ceux qu'on a listé mais qui appartiennent pas au cycle
    finalGrid = grids[posDansCycle + racineCycle]
    return calcScore(finalGrid)

def toKey(grid):
    k = ""
    for l in grid:
        k = k + "".join(l)
    return k

def partCycle(grid, off):
    newGrid = [l[:] for l in grid]
    if off == NORTH or off == WEST:
        for x in rLen(grid):
            for y in rLen(grid[x]):
                if grid[x][y] == "O":
                    rollDir(x, y, newGrid, off)
    else:
        # Si on pousse vers le bas ou la gauche, faut parcourir la grille en partant de l'autre coin
        # Sinon l'algo de rouli va pas marcher, 
        # les rochers se "bloquant" sur d'autres qui ont juste pas encore bougés
        for x in range(len(grid) - 1, -1, -1):
            for y in range(len(grid[0]) - 1, -1, -1):
                if grid[x][y] == "O":
                    rollDir(x, y, newGrid, off)
    return newGrid

def rollDir(x, y, newGrid, off):
    newGrid[x][y] = "."
    dX, dY = off
    lX, lY = len(newGrid), len(newGrid[0])
    while True:
        nX, nY = x + dX, y + dY
        if nX >= 0 and nX < lX and nY >= 0 and nY < lY:
            if newGrid[nX][nY] != ".":
                break
            else:
                x, y = nX, nY
        else:
            break
    newGrid[x][y] = "O"


def calcScore(grid):
    tot = 0
    for x in rLen(grid):
        disSouth = len(grid) - x
        for y in rLen(grid[x]):
            if grid[x][y] == "O":
                tot += disSouth
    return tot


print(day14())
print(day14Second())