
file = open("day3data.txt", "r")
dic = dict()
withinMultipleClaims = 0
claimCoordinates = []

for line in file:
    coordinates = []
    #get all needed data
    line.strip()
    id, rest = line.split('@')
    startx, rest = rest.split(',')
    starty, sizes = rest.split(':')
    xsize, ysize = sizes.split('x')
    
    startx = int(startx)
    starty = int(starty)
    xsize = int(xsize)
    ysize = int(ysize)

    #loop through the coordinates
    for i in range(0,xsize):
        for j in range(0,ysize):
            #without ',' the string representing the coordinates is not unique. 12345 can corrspond to 123,45 or 12,345 for instance
            coordinate = str(startx+i)+','+str(starty+j)
            coordinates.append(coordinate)
            if coordinate in dic:
                dic[coordinate]+=1
            else:
                dic[coordinate]=1

    claimCoordinates.append(coordinates)

#check how many 1x1 blocks are use more than once
for key in dic:
    if dic[key] > 1:
        withinMultipleClaims+=1

print(withinMultipleClaims)


#find the only non-overlapping claim:
uniqueClaim = -1
unique = False

for index, claim in enumerate(claimCoordinates):
    unique = True
    for coordinate in claim:
        if dic[coordinate] > 1:
            unique = False
            break
    if unique == True:
        uniqueClaim = index + 1
        break


print("Unique claim: " + str(uniqueClaim))