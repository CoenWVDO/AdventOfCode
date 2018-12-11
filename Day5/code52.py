import re
import string

f = open("input.txt", 'r')

content = f.read()

f.close()

abc = list(string.ascii_lowercase)

charArray = list(content)
lowestLenght = 99999999

for letter in abc:
    print letter
    for char in tempList[:]:
       if char == letter or char == letter.upper():
           tempList.remove(char)
    changedAmount = -1
    while changedAmount != 0:
        changedAmount = 0
        lenght = len(tempList)
        for i in range(1, lenght):
            if tempList[i-1].isupper():
                if tempList[i].islower():
                    if re.search(tempList[i-1], tempList[i], re.IGNORECASE):
                        tempList[i-1] = '#'
                        tempList[i] = '#'
                        changedAmount+=1
            else:
                if tempList[i].isupper():
                    if re.search(tempList[i-1], tempList[i], re.IGNORECASE):
                        tempList[i-1] = '#'
                        tempList[i] = '#'
                        changedAmount+=1

        for char in tempList[:]:
            if char == '#':
                tempList.remove(char)
    newLenght = len(tempList)
    if newLenght < lowestLenght:
        lowestLenght = newLenght
        print lowestLenght

print lowestLenght
