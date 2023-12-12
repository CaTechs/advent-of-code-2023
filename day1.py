from utils import *


def day1():
    content = loadFileByLine(1)
    sum = 0
    for l in content:
        for c in l:
            if c.isnumeric():
                first = c
                break
        for c in l[::-1]:
            if c.isnumeric():
                last = c
                break
        loc = (int(first)*10) + int(last)
        sum += loc
    return sum
    
def day1t():
    content = loadFileByLine(1, "")
    sum = 0
    for l in content:
        start = ""
        for c in l:
            if c.isnumeric():
                first = c
                break
            else:
                start += c
                v = testDigit(start, False)
                if v > 0:
                    first = v
                    break
        end = ""
        for c in l[::-1]:
            if c.isnumeric():
                last = c
                break
            else:
                end = c + end
                v = testDigit(end, True)
                if v > 0:
                    last = v
                    break
        loc = (int(first)*10) + int(last)
        print(l,loc)
        sum += loc
    return sum
      
    

def testDigit(s, last):
    for i in range(0,10):
        d = digit[i]
        v = extract(s, len(d), last)
        if (d == v):
            return i
    return -1
        

def extract(s, size, last):
    if not last:
        v =  s[-size:]
        return v
    else:
        return s[0: size]

digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    
    
print(day1())
print(day1t())