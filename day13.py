from utils import *

def day13():
    content = loadFileByLine(13, "")
    g = []
    tot = 0
    for l in content:
        if l == "":
            tot += testGrid(g)
            g = []
        else:
            g.append(l)
    if len(g) > 0:
        tot += testGrid(g)
    return tot


def testGrid(g):
    listSetMirrors = []
    for l in g:
        listSetMirrors.append(testLine(l))
    mirror = listSetMirrors[0]
    for m in listSetMirrors[1:]:
        mirror.intersection_update(m)
    if len(mirror) == 1:
        return mirror.pop()
    
    # Sinon, on cherche les colonnes
    listSetMirrors = []
    for p in range(len(g[0])):
        col = [g[k][p] for k in range(len(g))]
        listSetMirrors.append(testLine(col))
    mirror = listSetMirrors[0]
    for m in listSetMirrors[1:]:
        mirror.intersection_update(m)
    if len(mirror) == 1:
        return 100*mirror.pop()


def testLine(l):
    setMirrors = set()
    for p in range(len(l)):
        mirror = True
        k = 0
        while True:
            plus = p + k + 1
            minus = p - k
            if minus >= 0 and plus < len(l):
                if not l[minus] == l[plus]:
                    mirror = False
                    break
                k += 1
            else:
                break
        if mirror and k > 0:
            #Si k = 0, on était juste sur un bord et on a rien testé
            setMirrors.add(p + 1)
    return setMirrors

def day13Second():
    content = loadFileByLine(13, "")
    g = []
    tot = 0
    for l in content:
        if l == "":
            tot += testGridSecond(g)
            g = []
        else:
            g.append(l)
    if len(g) > 0:
        tot += testGridSecond(g)
    return tot

def testGridSecond(g, sec = False):
    posSeen = [set() for k in range(len(g[0]) + 1)]
    for nL in range(len(g)):
        l = g[nL]
        listSetMirrors = testLine(l)
        for m in listSetMirrors:
            print(m, len(posSeen))
            posSeen[m].add(nL)
    nbrLine = len(g)
    for pos in range(len(posSeen)):
        p = posSeen[pos]
        if len(p) == nbrLine - 1:
            # Toutes les lines ont une reflexion à cette colonne, sauf une
            nL = set(range(nbrLine)).difference(p).pop()
            res = testLineWithError(g[nL], pos - 1)
            if res:
                return pos
    ## On a pas réussi :(
    ## On rotate la grille pour que les colonnes deviennent ds lign et on retente
    if sec:
        return -1
    return 100*testGridSecond(rotate(g), True)

def rotate(g):
    res = []
    for y in range(len(g[0])):
        loc = [g[x][y] for x in range(len(g))]
        res.append(loc)
    return res


def testLineWithError(l, p):
    nbrError = 0
    k = 0
    while True:
        plus = p + k + 1
        minus = p - k
        if minus >= 0 and plus < len(l):
            if not l[minus] == l[plus]:
                # Ca ne match pas, mais on a le droit à un joker
                nbrError += 1
                if nbrError > 1:
                    break
            k += 1
        else:
            break
    # On ne doit avoir qu'une et une seule erreur
    return nbrError == 1

print(day13Second()) 
