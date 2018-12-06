
def CheckSame(str1, str2):
    charList1 = list(str1)
    charList2 = list(str2)
    amount = 0
    i = 0
    for char in charList1:
        if char == charList2[i]:
            amount += 1
        i += 1
    return amount

f = open("input.txt", "r")

stringList = []

for line in f:
    stringList.append(line.rstrip('\n'))

print CheckSame(stringList[0], stringList[1])
#for string in stringList: 
#    print string

    