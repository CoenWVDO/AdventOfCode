
def CheckDiff(str1, str2):
    charList1 = list(str1)
    charList2 = list(str2)
    amount = 0
    i = 0
    for char in charList1:
        if char != charList2[i]:
            amount += 1
        i += 1
    return amount

f = open("input.txt", "r")

stringList = []
stringList2 = []

for line in f:
    stringList.append(line.rstrip('\n'))

lowestDif = 100
finalstr1 = ""
finalstr2 = ""

for string1 in stringList:
    for string2 in stringList:
        number = CheckDiff(string1, string2)
        if number != 0:
            if number < lowestDif:
                lowestDif = number
                print lowestDif
                finalstr1 = string1
                finalstr2 = string2

print finalstr1 + ' - ' + finalstr2

charList1 = list(finalstr1)
charList2 = list(finalstr2)
totalStr = ""
i = 0
for char in charList1:
    if char == charList2[i]:
        totalStr += char
    i += 1

print "totalStr = " + totalStr