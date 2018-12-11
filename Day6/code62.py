f = open("input.txt", 'r')

class Cordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def checkDistance(x,y,cordinate):
    return abs(x - cordinate.x) + abs(y - cordinate.y)

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

areaSize = 0

for y in range(height):
    for x in range(width):
        totalDistance = 0 
        for key, value in cordinateList.items():
            totalDistance += checkDistance(x,y, value)
        if totalDistance < 10000:
            areaSize += 1
print(areaSize)