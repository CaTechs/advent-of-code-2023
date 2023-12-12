from utils import *
from math import lcm

def day8():
    content = loadFileByLine(8, "")
    dirs, content = content[0], content[2:]
    dictAdj = dict()
    for l in content:
        a, b = l.split(" = (")
        b = b[:-1]
        dictAdj[a] = b.split(", ")
    step = 0
    ld = len(dirs)
    pos = "AAA"
    while True:
        if pos == "ZZZ":
            return step
        d = dirs[step % ld]
        if d == "L":
            pos = dictAdj[pos][0]
        else:
            pos = dictAdj[pos][1]
        step += 1

def day8Second():
    content = loadFileByLine(8, "")
    dirs, content = content[0], content[2:]
    dictAdj = dict()
    allPos = set()
    for l in content:
        a, b = l.split(" = (")
        b = b[:-1]
        dictAdj[a] = b.split(", ")
        if a[-1] == "A":
            allPos.add(a)
    step = 0
    ld = len(dirs)
    dictRes = dict()
    for sPos in allPos:
        dictRes[sPos] = []
        pos = sPos
        step = 0
        while True:
            if pos[-1] == "Z":
                dictRes[sPos].append(step)
                if len(dictRes[sPos]) == 2:
                    break
            d = dirs[step % ld]
            if d == "L":
                pos = dictAdj[pos][0]
            else:
                pos = dictAdj[pos][1]
            step += 1
    print(dictRes)
    res = [v[0] for v in dictRes.values()]
    print(res)
    resLcm = 1
    for k in res:
        resLcm = lcm(resLcm, k)
    return resLcm




print(day8Second())