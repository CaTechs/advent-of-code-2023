from utils import *

# 526860 too low
# 528799
def day3():
    content = loadFileByLine(3, "")
    tot = 0
    n = ""
    engine = False
    for i in range(len(content)):
        if engine and n.isnumeric():
            print(n)
            tot += int(n)
        n = ""
        engine = False
        l = content[i]
        for j in range(len(l)):
            c = l[j]
            if c.isnumeric():
                n += c
                engine = engine or check(i, j, content)
            else:
                if engine and n.isnumeric():
                    print(n)
                    tot += int(n)
                n = ""
                engine = False
    return tot

def check(i, j, content):
    for y in [i -1, i, i + 1]:
        for x in [j - 1, j, j + 1]:
            if x == j and y == i:
                continue
            if y >= 0 and y < len(content) and x >= 0 and x < len(content[y]):
                c = content[y][x]
                if not c == "." and not c.isnumeric():
                    return True
    return False


def day3t():
    content = loadFileByLine(3, "")
    tot = 0
    n = ""
    engine = False
    dictGear = dict()
    setGear = set()
    for i in range(len(content)):
        n = ""
        engine = False
        l = content[i]
        for j in range(len(l)):
            c = l[j]
            if c.isnumeric():
                n += c
                checkTwo(i, j, content, setGear)
            else:
                if n.isnumeric():
                    print(n)
                    n = int(n)
                    for g in setGear:
                        if g not in dictGear:
                            dictGear[g] = []
                        dictGear[g].append(n)
                n = ""
                setGear = set()
        #fin de ligne
        if n.isnumeric():
            print(n)
            n = int(n)
            for g in setGear:
                if g not in dictGear:
                    dictGear[g] = []
                dictGear[g].append(n)
        n = ""
        setGear = set()
    tot = 0
    for x in dictGear.values():
        if len(x) == 2:
            tot += x[0]*x[1]
    return tot

def checkTwo(i, j, content, setGear):
    for y in [i -1, i, i + 1]:
        for x in [j - 1, j, j + 1]:
            if x == j and y == i:
                continue
            if y >= 0 and y < len(content) and x >= 0 and x < len(content[y]):
                c = content[y][x]
                if c == "*":
                    setGear.add((y,x))
    
print(day3t())
