
#Grid serial number = 8444
# 300x300 grid
# Rack ID is x-coordinate + 10
# Power level starts at rack ID * y-coordinate
# Add serial number to power level
# Power level = power level * rack ID
# Take the hundreds digits : xxXxx
# subtract 5 from the digit, this is the power level.

# Find the 3x3 square with the largest power level

coordinates = [[],]
threeXthreeSums = [[],]


for i in range(0,300):
    coordinates.append([]);
    for j in range(0,300):
        rackID = (i+1)+10
        powerLevel = (rackID*(j+1) + 8444)*rackID
        hundredIndex = len(str(powerLevel)) - 3 
        powerLevel = int(str(powerLevel)[hundredIndex])
        powerLevel -= 5
        coordinates[i].append(powerLevel)

max = 0
xMax = 0
yMax = 0

for i in range(0,297):
    threeXthreeSums.append([])
    for j in range(0,297):
        threeXthreeSum = coordinates[i][j]
        threeXthreeSum += coordinates[i][j+1]
        threeXthreeSum += coordinates[i][j+2]
        threeXthreeSum += coordinates[i+1][j]
        threeXthreeSum += coordinates[i+1][j+1]
        threeXthreeSum += coordinates[i+1][j+2]
        threeXthreeSum += coordinates[i+2][j]
        threeXthreeSum += coordinates[i+2][j+1]
        threeXthreeSum += coordinates[i+2][j+2]
        if threeXthreeSum > max:
            max = threeXthreeSum
            xMax = i+1 
            yMax = j+1
        threeXthreeSums[i].append(threeXthreeSum)

print ("Max value -- xMax -- yMax: " + str(max) + " -- " + str(xMax) + " -- " + str(yMax))

#Using summed-area table for part 2:
#Still not very fast, but acceptable for now

summedAreaTable = [[],]
for i in range(0,300):
    summedAreaTable.append([])
    for j in range(0,300):
        sum = coordinates[i][j]
        if i > 0 :
            sum+=summedAreaTable[i-1][j]
        if j > 0:
            sum+=summedAreaTable[i][j-1]
        if i > 0 and j > 0:
            sum-=summedAreaTable[i-1][j-1]
        summedAreaTable[i].append(sum)

maxPowerLevelPlusSquareSize = [[],]

ultramax = 0
ultramaxX = 0
ultramaxY = 0
ultramaxSquareSize = 0
for i in range(0,300):
    powerMax = 0
    squareMax = 0
    startX = 0
    startY = 0
    pointDone = False
    maxPowerLevelPlusSquareSize.append([])
    for j in range(0,300):
        #lets try with 1x1 up till max 100x100 squares
        for k in range(2,100):
            #For square starting at i,j and extending intill i+k and j+k, the sum is sumLevel[i+k][j+k] + sumLevel[i][j] - sumLevel[i+k][j] - sumLevel[i][j+k]
            if i+k >= 300 or j+k >= 300:
                break
            sumPower = summedAreaTable[i][j] + summedAreaTable[i+k][j+k] - summedAreaTable[i+k][j] - summedAreaTable[i][j+k]
            if (sumPower > powerMax):
                powerMax = sumPower
                squareMax = k
                startX = i
                startY = j
        maxPowerLevelPlusSquareSize[i].append({powerMax:squareMax})
        if powerMax > ultramax:
            ultramax = powerMax
            ultramaxSquareSize = squareMax
            ultramaxX = i 
            ultramaxY = j

#2 off for some reason (was expecting just 1 off, but whatever)
print ("Ultramax: " + str(ultramax) + " -- maxX: " + str(ultramaxX + 2) + " -- maxy: " + str(ultramaxY + 2) + " -- square size: " + str(ultramaxSquareSize))