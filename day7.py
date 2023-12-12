from utils import *

FIVE_OF = 7
FOUR_OF = 6
FULL_HOUSE = 5
THREE_OF = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH = 1

dictCardValue = {
	"1" : "A",
	"2" : "B",
	"3" : "C",
	"4" : "D",
	"5" : "E",
	"6" : "F",
	"7" : "G",
	"8" : "H",
	"9" : "I",
	"T" : "J",
	"J" : "K",
	"Q" : "L",
	"K" : "M",
	"A" : "N",
}
dictCardValueSecond = {
	"J" : "A",
	"1" : "B",
	"2" : "C",
	"3" : "D",
	"4" : "E",
	"5" : "F",
	"6" : "G",
	"7" : "H",
	"8" : "I",
	"9" : "J",
	"T" : "K",
	"Q" : "L",
	"K" : "M",
	"A" : "N",
}

def day7():
    content = loadFileByLine(7, "")
    hands = []
    for l in content:
    	hand, bid = l.split(" ")
    	hands.append((rankHand(hand), hand, bid))
    print(hands)
    hands = sorted(hands, key = extract)
    print(hands)
    tot = 0
    for i in range(len(hands)):
    	tot += (i+1) * int(hands[i][-1])
    return tot

def extract(hand):
	return (hand[0], [dictCardValue[i] for i in hand[1]])

def rankHand(hand):
	dictOccu = dict()
	for c in hand:
		dictOccu[c] = dictOccu.get(c, 0) + 1
	count = [0 for i in range(5)]
	for v in dictOccu.values():
		count[v - 1] += 1
	if count[4] == 1:
		## Five of a kind
		return FIVE_OF
	if count[3] == 1:
		return FOUR_OF
	if count[2] == 1:
		if count[1] == 1:
			return FULL_HOUSE
		else:
			return THREE_OF
	if count[1] == 2:
		return TWO_PAIR
	if count[1] == 1:
		return ONE_PAIR
	return HIGH

def day7Second():
    content = loadFileByLine(7, "")
    hands = []
    for l in content:
    	hand, bid = l.split(" ")
    	hands.append((rankHandSecond(hand), hand, bid))
    print(hands)
    hands = sorted(hands, key = extractSecond)
    print(hands)
    tot = 0
    for i in range(len(hands)):
    	tot += (i+1) * int(hands[i][-1])
    return tot

def extractSecond(hand):
	return (hand[0], [dictCardValueSecond[i] for i in hand[1]])

def rankHandSecond(hand):
	dictOccu = dict()
	for c in hand:
		dictOccu[c] = dictOccu.get(c, 0) + 1
	nbrJoker = dictOccu.get("J", 0)
	count = [0 for i in range(5)]
	dictOccu["J"] = 0
	dictOccu.pop("J")
	bestPos = 0
	for v in dictOccu.values():
		count[v - 1] += 1
		if (v - 1) > bestPos:
			bestPos = v - 1
	bCount = count[:]
	count[bestPos] -= 1
	if nbrJoker == 5:
		count[-1] = 1
	else:
		count[bestPos + nbrJoker] += 1

	if count[4] == 1:
		## Five of a kind
		return FIVE_OF
	if count[3] == 1:
		return FOUR_OF
	if count[2] == 1:
		if count[1] == 1:
			return FULL_HOUSE
		else:
			return THREE_OF
	if count[1] == 2:
		return TWO_PAIR
	if count[1] == 1:
		return ONE_PAIR
	return HIGH

# 249192333 too low
# 249400220
print(day7Second())