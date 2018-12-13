class Step:
    def __init__(self, first, then):
        self.first = first
        self.then  = then


class LinkedItem:
    def __init__(self, id, time):
        self.prev = []
        self.id = id
        self.time = time + 60
        self.workDone = False

    def addPrev(self, prev):
        self.prev.append(prev)

    def removePrev(self, prev):
        self.prev.remove(prev)

    def getPrevSize(self):
        return len(self.prev)

    def work(self):
        self.time -= 1
        if self.time <= 0:
            self.workDone = True

import string

f = open("input.txt", 'r')

orderList = []

for line in f:
    tempSplit = line.split()
    orderList.append(Step(tempSplit[1], tempSplit[7]))


linkedItemList = []

abc = list(string.ascii_uppercase)

abcValues = {}

letterValue = 1
for letter in abc:
    abcValues[letter] = letterValue
    letterValue+=1


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
        linkedItemList.append(LinkedItem(order.then, abcValues[order.then]))
    if firstFound == False:
        linkedItemList.append(LinkedItem(order.first, abcValues[order.first]))

for order in orderList:
    for linkedItem in linkedItemList:
        if linkedItem.id == order.then:
            linkedItem.addPrev(order.first)

nextInLineList = []

for linkedItem in linkedItemList:
    if linkedItem.getPrevSize() == 0:
        nextInLineList.append(linkedItem.id)

workerAmount = 2

totalSecond = 0

while len(nextInLineList) > 0:
    nextInLineList.sort()
    for i in range(workerAmount):
        if i >= len(nextInLineList):
            break
        for item in linkedItemList:
            if item.id == nextInLineList[i]:
                tempWorker = item
                tempWorker.work()
                if tempWorker.workDone:
                    for linkedItem in linkedItemList:
                        if nextInLineList[i] in linkedItem.prev:
                            linkedItem.removePrev(nextInLineList[i])
                            if linkedItem.getPrevSize() == 0:
                                nextInLineList.append(linkedItem.id)
                    nextInLineList[i] = '#'
                    break
    for worker in nextInLineList:
        if worker == '#':
            nextInLineList.remove(worker)
    
    totalSecond += 1

print(totalSecond)