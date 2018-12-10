import re

f = open("input.txt", 'r')

content = f.read()
f.close()

charArray = list(content)
changedAmount = -1
while changedAmount != 0:
    changedAmount = 0
    lenght = len(charArray)
    for i in range(1, lenght):
        if charArray[i-1].isupper():
            if charArray[i].islower():
                if re.search(charArray[i-1], charArray[i], re.IGNORECASE):
                    charArray[i-1] = '#'
                    charArray[i] = '#'
                    changedAmount+=1
        else:
            if charArray[i].isupper():
                if re.search(charArray[i-1], charArray[i], re.IGNORECASE):
                    charArray[i-1] = '#'
                    charArray[i] = '#'
                    changedAmount+=1

    for char in charArray[:]:
        if char == '#':
            charArray.remove(char)

print ''.join(charArray)
print len(charArray)
