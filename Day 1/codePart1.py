f = open("input.txt", "r")
totalNumber = 0

for line in f:
    totalNumber = totalNumber + int(line)
print totalNumber