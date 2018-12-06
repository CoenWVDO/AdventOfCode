#from timeit import default_timer as timer

#start = timer()

totalNumber = 0
totalNumbers = set()
inputList = []
found = False

f = open("input.txt", "r")
for line in f:
    inputList.append(int(line))
f.close()


while found == False: 
    for listNumber in inputList:
        totalNumber = totalNumber + listNumber
        if totalNumber in totalNumbers:
            print "First Freqeunce twice -> " + str(totalNumber)
            found = True
            break
        totalNumbers.add(totalNumber)
#stop = timer()

#print (stop - start)