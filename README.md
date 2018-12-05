# AdventOfCode

from timeit import default_timer as timer
start = timer()
 
file = open("day2data.txt", "r")
nrOfTwo = 0
nrOfThree = 0
 
for line in file:
    two = False
    three = False
    for character in line:
            dic[character]+=1
    for key in dic:
        if dic[key] == 2:
            two = True
        elif dic[key] == 3:
            three = True
        dic[key] = 0
    if two:
        nrOfTwo+=1
    if three:
        nrOfThree+=1
    
print(nrOfTwo*nrOfThree)
end = timer()
print ("Time passed: " + str(end-start)) 
