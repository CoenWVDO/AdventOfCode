class Step:
    def __init__(self, first, then):
        self.first = first
        self.then  = then


class LinkedItem:
    def __init__(self, id):
        self.prev = []
        self.id = id

    def addPrev(self, prev):
        self.prev.append(prev)

    def removePrev(self, prev):
        self.prev.remove(prev)

    def getPrevSize(self):
        return len(self.prev)

import string

f = open("input.txt", 'r')

orderList = []

for line in f:
    tempSplit = line.split()
    orderList.append(Step(tempSplit[1], tempSplit[7]))


linkedItemList = []

for order in orderList:
    thenFound = False
    firstFound = False
    for linkedItem in linkedItemList:
        if linkedItem.id == order.then:
            thenFound = True
            if firstFound:
                break
        if linkedItem.id == order.first:
            firstFound = True
            if thenFound:
                break
    if thenFound == False:
        linkedItemList.append(LinkedItem(order.then))
    if firstFound == False:
        linkedItemList.append(LinkedItem(order.first))

for order in orderList:
    for linkedItem in linkedItemList:
        if linkedItem.id == order.then:
            linkedItem.addPrev(order.first)

nextInLineList = []

for linkedItem in linkedItemList:
    if linkedItem.getPrevSize() == 0:
        nextInLineList.append(linkedItem.id)

finalString = ""
totalSecond = 0
minite = 60

abc = list(string.ascii_uppercase)

abcValues = {}

letterValue = 0
for letter in abc:
    abcValues[letter] = letterValue
    letterValue+=1

while len(nextInLineList) > 0:
    nextInLineList.sort()
    finalString += nextInLineList[0]
    for linkedItem in linkedItemList:
        if nextInLineList[0] in linkedItem.prev:
            linkedItem.removePrev(nextInLineList[0])
            if linkedItem.getPrevSize() == 0:
                nextInLineList.append(linkedItem.id)
    nextInLineList.pop(0)


print(finalString)