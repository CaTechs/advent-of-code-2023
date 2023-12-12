from utils import *

def day6():
    content = loadFileByLine(6, "")
    time, distance = content
    time = parseList(time)
    distance = parseList(distance)
    tot = 1
    for i in range(len(time)):
        t, d = time[i], distance[i]
        tot *= race(t, d)
    return tot

def day6t():
    content = loadFileByLine(6, "")
    time, distance = content
    time = parseListSecond(time)
    distance = parseListSecond(distance)
    tot = race(time, distance)
    return tot


def race(time, distance):
    res = 0
    for k in range(time):
        d = k*(time-k)
        if d > distance:
            res += 1
        elif res > 0:
            # On a dépassé le secteur où ça marche, pas la peine de compter jusqu'au bout
            break

    return res






def parseList(time):
    time = time.split(":")[1]
    time = time.split(" ")
    realTime = []
    for t in time:
        if not t == "":
            realTime.append(int(t))
    return realTime

def parseListSecond(time):
    time = time.split(":")[1]
    time = time.split(" ")
    realTime = ""
    for t in time:
        if not t == "":
            realTime += t
    return int(realTime)

print(day6())
print(day6t())
