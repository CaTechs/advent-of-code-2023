from utils import *

def day4():
    content = loadFileByLine(4, "")
    tot = 0
    for l in content:
        l = l.split(": ")[1]
        win, got = l.split(" | ")
        win, got = set(win.split(" ")), set(got.split(" "))
        win.discard("")
        got.discard("")
        inter = win.intersection(got)
        nbrWin = len(inter)
        if nbrWin > 0:
            tot += 2**(nbrWin - 1)
    return tot
    
def day4t():
    content = loadFileByLine(4, "")
    tot = 0
    nbrCard = dict()
    for i in range(len(content)):
        l = content[i]
        c = nbrCard.get(i, 0) + 1
        tot += c
        win, got = l.split(" | ")
        win, got = set(win.split(" ")), set(got.split(" "))
        win.discard("")
        got.discard("")
        inter = win.intersection(got)
        nbrWin = len(inter)
        for k in range(nbrWin):
            pos = i + k + 1
            nbrCard[pos] = nbrCard.get(pos, 0) + c
    return tot

print(day4t())