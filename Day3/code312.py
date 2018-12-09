class SquareInfo:
    def __init__(self, id, spaceX, spaceY, sizeX, sizeY):
        self.id = id
        self.spaceX = spaceX
        self.spaceY = spaceY
        self.sizeX = sizeX
        self.sizeY = sizeY


f = open("input.txt", "r")

SquareInfoList = set()

for line in f:
    infoString = line.rstrip('\n')
    splitInfo = infoString.split()
    spaceSplit = splitInfo[2].split(',')
    sizeSplit = splitInfo[3].split('x')
    SquareInfoList.add(SquareInfo(
        splitInfo[0], int(spaceSplit[0]), int(spaceSplit[1].rstrip(':')), int(sizeSplit[0]), int(sizeSplit[1])))

field = []
for f in range(1000):
    row = ""
    for i in range(1000):
        row += '.'
    field.append(list(row))

for square in SquareInfoList:
    for y in range(square.spaceY, square.spaceY + square.sizeY):
        for x in range(square.spaceX, square.spaceX + square.sizeX):
            if field[y][x] == '#' or field[y][x] == 'x':
                field[y][x] = 'x'
            else:
                field[y][x] = '#'

xAmount = 0
for i in range(1000):
    for j in range(1000):
        if field[i][j] == 'x':
            xAmount += 1

print xAmount

# part2
theOne = True

for square in SquareInfoList:
    for y in range(square.spaceY, square.spaceY + square.sizeY):
        for x in range(square.spaceX, square.spaceX + square.sizeX):
            if field[y][x] == 'x':
                theOne = False
                break
        if theOne == False:
            break
    if theOne == True:
        print square.id
    theOne = True
