from utils import *

def day5():
    content = loadFileByLine(5, "")
    seed, content = content[0], content[3:]
    seed = seed.split(": ")[1]
    currentCat = [int(s) for s in seed.split(" ")]
    currentSet = set(currentCat)
    nextCat = []
    for l in content:
        if l == "":
            # fin de bloc
            for c in currentSet:
                nextCat.append(c)
            currentCat = nextCat
            currentSet = set(currentCat)
            nextCat= []
            continue
        elif not l[0].isnumeric():
            #Description, on skip
            continue
        startNext, startCurrent, size = [int(n) for n in l.split(" ")]
        dif = startNext - startCurrent
        for s in currentCat:
            if s >= startCurrent and s < (startCurrent + size):
                nextCat.append(s + dif)
                currentSet.discard(s)
                
    print(nextCat)
    return min(nextCat)

# 3014768818 too high
# 41222968
def day5t():
    content = loadFileByLine(5, "")
    seed, content = content[0], content[2:]
    seed = seed.split(": ")[1]
    seed = [int(s) for s in seed.split(" ")]
    currentCat = []
    for i in range(0, len(seed), 2):
        a,b = seed[i], seed[i+1]
        currentCat.append((a, a + b - 1))
    print(currentCat)
    nextCat = []
    for l in content:
        if l == "":
            # fin de bloc
            # N'ont pas shift, on les passe tel quel
            nextCat.extend(currentCat)
            currentCat = nextCat
            nextCat= []
            continue
        elif not l[0].isnumeric():
            #Description, on skip
            print(l)
            continue
        startNext, startCurrent, size = [int(n) for n in l.split(" ")]
        shift = startNext - startCurrent
        shiftRange = (startCurrent, startCurrent + size - 1)
        newCurrentCat = []
        for s in currentCat:
            cur, nex = calcInter(s, shiftRange, shift)
            newCurrentCat.extend(cur)
            nextCat.extend(nex)
        currentCat = newCurrentCat
    if len(nextCat) > 0: #On a pas pris le temps de décaler avant de finir, donc je le fais
        currentCat = nextCat
    return min([s[0] for s in currentCat])
   
def calcInter(first, second, shift):
    a,b = first
    x,y = second
    notChanged = []
    news = []
    if isPointInBetween(a, x, y) and isPointInBetween(b, x, y):
        # Les graines sont entierement contenues dans l'almanach
        news.append((a + shift, b + shift)) # Donc tout le bloc shift
    elif isPointInBetween(x, a, b) and isPointInBetween(y, a, b):
        # L'almanach est contenu dans les graines
        notChanged.append((a, x - 1)) # Ce qui dépasse à gauche ne shift pas
        notChanged.append((y + 1, b)) # Ce qui dépasse à droite ne shift pas
        news.append((x + shift, y + shift)) # L'intégralité de l'almanach shift
    elif not isPointInBetween(a, x, y) and isPointInBetween(b, x, y):
        # Les graines recoupent par la gauche de l'almanach
        notChanged.append((a, x-1)) # Ce qui dépasse à gauche ne shift pas
        news.append((x + shift, b + shift)) # La partie de droite shift
    elif isPointInBetween(a, x, y) and not isPointInBetween(b, x, y):
            # Les graines recoupent par la droite de l'almanach
        notChanged.append((y + 1, b))
        news.append((a + shift, y + shift))
    else:
        # Aucune forme de match
        notChanged.append((a, b)) 
    
    return (notChanged, news)
  
def isPointInBetween(x, a, b):
    return a <= x and x <= b


if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    print(day5t())
