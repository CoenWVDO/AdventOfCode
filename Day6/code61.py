f = open("input.txt", 'r')

class Cordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def checkDistance(x,y,cordinate):
    return abs(x - cordinate.x) + abs(y - cordinate.y)

def checkIfFinite(width, height, key, field):
    for i in range (width):
        if key == field[0][i] or key == field[height-1][i]:
            return False
    for i in range (height):
        if key == field[i][0] or key == field[i][width-1]:
            return False
    return True

cordinateList = dict()

idCounter = 1
for line in f:
    line = line.strip('\n')
    cordinateList[idCounter] = Cordinate(int(line.split(',')[0]), int(line.split()[1]))
    idCounter += 1

f.close()

width = 0
height = 0

for key, value in cordinateList.items():
    if value.x > width:
        width = value.x
    if value.y > height:
        height = value.y

width +=1
height +=1

field = []
for y in range(height):
    row = []
    for x in range(width):
        row.append(0)
    field.append(row)


for key, value in cordinateList.items():
    field[value.y][value.x] = key

for y in range(height):
    for x in range(width):
        if field[y][x] == 0:
            distance = 0
            lowestDistance = width*height
            id = 0
            for key, value in cordinateList.items():
                distance = checkDistance(x,y, value)
                if distance < lowestDistance:
                    lowestDistance = distance
                    id = key
                elif distance == lowestDistance:
                    id = -1
            field[y][x] = id    
largestArea  = 0
for key, value in cordinateList.items():
    areaCount = 0
    for y in range(height):
        for x in range(width):
            if field[y][x] == key:
                areaCount += 1
    if areaCount > largestArea:
        if checkIfFinite(width, height, key, field):
            largestArea = areaCount
print(largestArea)