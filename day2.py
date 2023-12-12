from utils import *


def day2():
    content = loadFileByLine(2)
    mr, mg, mb = 12,13,14
    i = 1
    tot = 0
    for l in content:
        l = l.split(": ")[1]
        l = l.split("; ")
        possible = True
        for b in l:
            b = b.split(", ")
            for cube in b:
                value, color = cube.split(" ")
                value = int(value)
                if color == "blue" and value > mb:
                    possible = False
                elif color == "green" and value > mg:
                    possible = False
                elif color == "red" and value > mr:
                    possible = False    
                
                
        
        if possible:
            tot += i
        
        
        i +=1
    
    return tot
    
    
def day2t():
    content = loadFileByLine(2)
    tot = 0
    for l in content:
        l = l.split(": ")[1]
        l = l.split("; ")
        mr, mg, mb = 0, 0, 0
        for b in l:
            b = b.split(", ")
            for cube in b:
                value, color = cube.split(" ")
                value = int(value)
                if color == "blue":
                    mb = max(mb, value)
                elif color == "green":
                    mg = max(mg, value)
                elif color == "red":
                    mr = max(mr, value) 
        tot += mr*mg*mb
        
            
    return tot
print(day2())
print(day2t())