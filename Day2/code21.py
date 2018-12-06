def CheckForTwo(str):
    found = False
    charList = list(str)   
    for char in charList:
        if str.count(char) == 2:
            return True
    return False

def CheckForThree(str):
    found = False
    charList = list(str)   
    for char in charList:
        if str.count(char) == 3:
            return True
    return False

f = open("input.txt", "r")
totalTwo = 0
totalThree = 0


for line in f:
    if CheckForTwo(line):
        totalTwo += 1
    if CheckForThree(line):
        totalThree += 1

print totalTwo * totalThree
