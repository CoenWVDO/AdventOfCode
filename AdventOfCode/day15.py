

elvesAlive = 0
goblinsAlive = 0

class Space:
    def __init__(self, entity):
        self.type = type
        self.entity = entity

    def setSpace(self, entity):
        self.entity = entity

    def setFighter(self, fighter):
        self.fighter = fighter

class Field:
    def __init__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize
        self.spaces = []
        for i in range(0,xSize):
            self.spaces.append([])
            for j in range(0, ySize):
                self.spaces[i].append(0)

    def addSpace(self, x, y, space):
        self.spaces[x][y] = space

    def changeSpace(self, x, y, entity):
        self.spaces[x][y].setSpace(entity)
   

class Fighter:
    def __init__(self, xPos, yPos, entity):
        self.enemyAdjacent = False
        self.hp = 200
        self.xPos = xPos
        self.yPos = yPos
        self.entity = entity
        self.alive = True

    def __eq__(self, other):
        return (self.xPos == other.xPos and self.yPos == other.yPos)

    def __lt__(self, other):
        if self.yPos == other.yPos:
            return self.xPos < other.xPos
        else:
            return self.yPos < other.yPos


data = []
yCount = 0
file = open("day15data.txt", "r")

for line in file:
    xCount = len(line)
    data.append(line)
    yCount+=1

field = Field(xCount, yCount)
fighters = []   

y = -1
for line in data:
    y+=1
    x= -1
    for ch in line:
        x+=1
        if ch == '#':
            spa = Space(-1)
            field.addSpace(x, y, spa)
        elif ch == ".":
            spa = Space(0)
            field.addSpace(x, y, spa)
        elif ch == "G":
            spa = Space(1)
            field.addSpace(x, y, spa)
            figh = Fighter(x, y, 1)
            fighters.append(figh)
            field.spaces[x][y].setFighter(figh)
            goblinsAlive+=1
        elif ch == "E":
            spa = Space(2)
            field.addSpace(x, y, spa)
            figh = Fighter(x, y, 2)
            fighters.append(figh)
            field.spaces[x][y].setFighter(figh)
            elvesAlive+=1

"""
adjacencyMap = {(0,0):[(0,0),],}

#Dijkstra, construction adjacency map for the first time:
#key should be [x,y], values should be [[x,y],[x,y],etc]
for i in range(0, field.xSize):
    for j in range(0, field.ySize):
        spa = field.spaces[i][j]
        if spa.entity == 0:
            adjacencyMap[(i,j)] = []
            if field.spaces[i][j-1].entity == 0:
                adjacencyMap[(i,j)].append((i,j-1))
            if field.spaces[i+1][j].entity == 0:
                adjacencyMap[(i,j)].append((i+1,j))
            if field.spaces[i-1][j].entity == 0:
                adjacencyMap[(i,j)].append((i-1,j))
            if field.spaces[i][j+1].entity == 0:
                adjacencyMap[(i,j)].append((i,j+1))

adjacencyMap.pop((0,0))
"""

def dijkstra(start):
    distanceDict = {}
    for i in range(0, field.xSize):
        for j in range(0, field.ySize):
            if (field.spaces[i][j].entity == 0):
                distanceDict[(i,j)] = [100000,]

    workSet = dict()
    workSet[start] = 0

    neighbours = []
    i = start[0]
    j = start[1]
    if field.spaces[i][j-1].entity == 0:
        neighbours.append((i,j-1))
    if field.spaces[i+1][j].entity == 0:
        neighbours.append((i+1,j))
    if field.spaces[i-1][j].entity == 0:
        neighbours.append((i-1,j))
    if field.spaces[i][j+1].entity == 0:
        neighbours.append((i,j+1))

    n = 0
    while(len(workSet) > 0):
        coord = min(workSet, key=workSet.get)
        distance = workSet.pop(coord)
        if n > 0:
            for neighbour in adjacencyMap[coord]:
                if distance + 1 < distanceDict[neighbour][0]:
                    distanceDict[neighbour][0] = distance + 1
                    workSet[neighbour] = distance+1
                    distanceDict[neighbour][1:] = distanceDict[coord][1:]
                    distanceDict[neighbour].append(neighbour)
        else:
            for neighbour in neighbours:
                if distance + 1 < distanceDict[neighbour][0]:
                    distanceDict[neighbour][0] = distance + 1
                    workSet[neighbour] = distance+1
                    if coord != start:
                        distanceDict[neighbour][1:] = distanceDict[coord][1:]
                    distanceDict[neighbour].append(neighbour)
                    n+=1
    return distanceDict

distance = 10000
route = []
allDead = False

"""
def fighterdied(i, j):
    return
    field.spaces[i][j].entity = 0
    adjacencyMap[(i,j)] = []
    if (i+1,j) in adjacencyMap:
        adjacencyMap[(i+1,j)].append((i,j))
    elif field.spaces[i+1][j].entity == 0:
        adjacencyMap[(i+1,j)] = [(i,j),]
    if (i-1,j) in adjacencyMap:
        adjacencyMap[(i-1,j)].append((i,j))
    elif field.spaces[i-1][j].entity == 0:
        adjacencyMap[(i-1,j)] = [(i,j),]
    if (i,j+1) in adjacencyMap:
        adjacencyMap[(i,j+1)].append((i,j))
    elif field.spaces[i][j+1].entity == 0:
        adjacencyMap[(i,j+1)] = [(i,j),]
    if (i,j-1) in adjacencyMap:
        adjacencyMap[(i,j-1)].append((i,j))
    elif field.spaces[i][j-1].entity == 0:
        adjacencyMap[(i,j-1)] = [(i,j),]

    if field.spaces[i][j-1].entity == 0:
        adjacencyMap[(i,j)].append((i,j-1))
    if field.spaces[i+1][j].entity == 0:
        adjacencyMap[(i,j)].append((i+1,j))
    if field.spaces[i-1][j].entity == 0:
        adjacencyMap[(i,j)].append((i-1,j))
    if field.spaces[i][j+1].entity == 0:
        adjacencyMap[(i,j)].append((i,j+1))

    if (field.spaces[i+1][j].entity == 1 or field.spaces[i-1][j].entity == 1
        or field.spaces[i][j+1].entity == 1 or field.spaces[i][j-1].entity == 1):
        elfDestinations.append((i,j))

    if (field.spaces[i+1][j].entity == 2 or field.spaces[i-1][j].entity == 2
        or field.spaces[i][j+1].entity == 2 or field.spaces[i][j-1].entity == 2):
        goblinDestinations.append((i,j))


def updateAdj(moveFrom, moveTo, entity):
    return
    fromX = moveFrom[0]
    fromY = moveFrom[1]
    toX = moveTo[0]
    toY = moveTo[1]

    field.spaces[fromX][fromY].entity = 0
    field.spaces[toX][toY].entity = entity

    #Add the FROM coordinates to the adjacency map
    adjacencyMap[(fromX, fromY)] = []
    if field.spaces[fromX][fromY-1].entity == 0:
        adjacencyMap[(fromX,fromY)].append((fromX,fromY-1))
    if field.spaces[fromX+1][fromY].entity == 0:
        adjacencyMap[(fromX,fromY)].append((fromX + 1,fromY))
    if field.spaces[fromX-1][fromY].entity == 0:
        adjacencyMap[(fromX,fromY)].append((fromX-1,fromY))
    if field.spaces[fromX][fromY+1].entity == 0:
        adjacencyMap[(fromX,fromY)].append((fromX,fromY+1))

    #Add the FROM coordinates to the neighbours of the FROM, will possibly be added to the TO-entry but this entry will be removed anyway in the next step
    if (fromX-1, fromY) in adjacencyMap:
        adjacencyMap[(fromX-1, fromY)].append((fromX, fromY))
    elif field.spaces[fromX-1][fromY].entity == 0:
        adjacencyMap[(fromX-1, fromY)] = [(fromX, fromY),]

    if (fromX+1, fromY) in adjacencyMap:
        adjacencyMap[(fromX+1, fromY)].append((fromX, fromY))
    elif field.spaces[fromX+1][fromY].entity == 0:
        adjacencyMap[(fromX+1, fromY)] = [(fromX, fromY),]

    if (fromX, fromY-1) in adjacencyMap:
        adjacencyMap[(fromX, fromY-1)].append((fromX, fromY))
    elif field.spaces[fromX][fromY-1].entity == 0:
        adjacencyMap[(fromX, fromY-1)] = [(fromX, fromY),]

    if (fromX, fromY+1) in adjacencyMap:
        adjacencyMap[(fromX, fromY+1)].append((fromX, fromY))
    elif field.spaces[fromX][fromY+1].entity == 0:
        adjacencyMap[(fromX, fromY+1)] = [(fromX, fromY),]

    #remove the TO coordinates from the adjacency map
    if (toX, toY) in adjacencyMap:
        adjacencyMap.pop((toX, toY))

    #remove the TO coordinates from all the neighbours that contain them
    if (toX+1, toY) in adjacencyMap:
        if (toX, toY) in adjacencyMap[(toX+1, toY)]:
            adjacencyMap[(toX+1, toY)].remove((toX, toY))

    if (toX-1, toY) in adjacencyMap:
        if (toX, toY) in adjacencyMap[(toX-1, toY)]:
            adjacencyMap[(toX-1, toY)].remove((toX, toY))

    if (toX, toY+1) in adjacencyMap:
        if (toX, toY) in adjacencyMap[(toX, toY+1)]:
            adjacencyMap[(toX, toY+1)].remove((toX, toY))

    if (toX, toY-1) in adjacencyMap:
        if (toX, toY) in adjacencyMap[(toX, toY-1)]:
            adjacencyMap[(toX, toY-1)].remove((toX, toY))

    #change the destinations
    destinations = goblinDestinations
    if entity == 1:
        destinations = elfDestinations

    if (fromX+1, fromY) in destinations:
        destinations.remove((fromX+1, fromY))
    if (fromX-1, fromY) in destinations:
        destinations.remove((fromX-1, fromY))
    if (fromX, fromY+1) in destinations:
        destinations.remove((fromX, fromY+1))
    if (fromX, fromY-1) in destinations:
        destinations.remove((fromX, fromY-1))

    if field.spaces[toX+1][toY].entity == 0:
        destinations.append((toX+1,toY))
    if field.spaces[toX-1][toY].entity == 0:
        destinations.append((toX-1,toY))
    if field.spaces[toX][toY+1].entity == 0:
        destinations.append((toX,toY+1))
    if field.spaces[toX][toY-1].entity == 0:
        destinations.append((toX,toY-1))

"""


counter = 0
while allDead == False:
    
       
    for i in range(0,field.xSize):
        output = ""
        for j in range(0,field.ySize):
            sp = field.spaces[j][i]
            if sp.entity == -1:
                output+='#'
            elif sp.entity == 0:
                output+='.'
            elif sp.entity == 1:
                output+='G'
            elif sp.entity == 2:
                output+='E'
        print(output)
    print('\n')
    
    if (counter > 90):
        breakpoint = 1

  #  fighters = sorted(fighters)
    for j,fig in enumerate(fighters):
        #deleteIndices = []
        #for i,f in enumerate(fighters):
        #    if f.hp < 1:
        #        deleteIndices.append(i)
        #deleteIndices = reversed(deleteIndices)

        #for i in deleteIndices:
        #    fighters.pop(i)

        f = fighters[j]

        """
        for i in range(0,field.xSize):
            output = ""
            for j in range(0,field.ySize):
                sp = field.spaces[j][i]
                if sp.entity == -1:
                    output+='#'
                elif sp.entity == 0:
                    output+='.'
                elif sp.entity == 1:
                    output+='G'
                elif sp.entity == 2:
                    output+='E'
            print(output)
        print('\n')
        """

        if f.entity == 2:
            breakpoints = 2
        if f.hp > 0:
            goblinDestinations = []
            elfDestinations = []
            for a,g in enumerate(fighters):
                if g.hp > 0:
                    pos = [g.xPos, g.yPos]
                    xPos = g.xPos
                    yPos = g.yPos
                    if g.entity == 2:
                        if field.spaces[xPos+1][yPos].entity == 0:
                            goblinDestinations.append((xPos+1, yPos))
                        if field.spaces[xPos-1][yPos].entity == 0:
                            goblinDestinations.append((xPos-1, yPos))
                        if field.spaces[xPos][yPos+1].entity == 0:
                            goblinDestinations.append((xPos, yPos+1))
                        if field.spaces[xPos][yPos-1].entity == 0:
                            goblinDestinations.append((xPos, yPos-1))
                    elif g.entity == 1:
                        if field.spaces[xPos+1][yPos].entity == 0:
                            elfDestinations.append((xPos+1, yPos))
                        if field.spaces[xPos-1][yPos].entity == 0:
                            elfDestinations.append((xPos-1, yPos))
                        if field.spaces[xPos][yPos+1].entity == 0:
                            elfDestinations.append((xPos, yPos+1))
                        if field.spaces[xPos][yPos-1].entity == 0:
                            elfDestinations.append((xPos, yPos-1)) 

            adjacencyMap = {(0,0):[(0,0),],}
            
            #Dijkstra, construction adjacency map for the first time:
            #key should be [x,y], values should be [[x,y],[x,y],etc]
            for i in range(0, field.xSize):
                for j in range(0, field.ySize):
                    spa = field.spaces[i][j]
                    if spa.entity == 0:
                        adjacencyMap[(i,j)] = []
                        if field.spaces[i][j-1].entity == 0:
                            adjacencyMap[(i,j)].append((i,j-1))
                        if field.spaces[i+1][j].entity == 0:
                            adjacencyMap[(i,j)].append((i+1,j))
                        if field.spaces[i-1][j].entity == 0:
                            adjacencyMap[(i,j)].append((i-1,j))
                        if field.spaces[i][j+1].entity == 0:
                            adjacencyMap[(i,j)].append((i,j+1))

            adjacencyMap.pop((0,0))
            if f.entity == 2:
                breakpoint = 2

            minDistance = 10000000
            distances = dijkstra((f.xPos, f.yPos))
            entity = 0
            selected = 0
            fight = 0
            selectedHp = 1000
            if field.spaces[f.xPos][f.yPos-1].entity + f.entity == 3:
                if field.spaces[f.xPos][f.yPos-1].fighter.hp > 0:
                    selected = 1
                    selectedHp = field.spaces[f.xPos][f.yPos-1].fighter.hp
            if field.spaces[f.xPos-1][f.yPos].entity + f.entity == 3:
                if field.spaces[f.xPos-1][f.yPos].fighter.hp < selectedHp and field.spaces[f.xPos-1][f.yPos].fighter.hp > 0:
                    selected = 2
                    selectedHp = field.spaces[f.xPos-1][f.yPos].fighter.hp
            if field.spaces[f.xPos+1][f.yPos].entity + f.entity == 3:
                if field.spaces[f.xPos+1][f.yPos].fighter.hp < selectedHp and field.spaces[f.xPos+1][f.yPos].fighter.hp > 0:
                    selected = 3
                    selectedHp = field.spaces[f.xPos+1][f.yPos].fighter.hp
            if field.spaces[f.xPos][f.yPos+1].entity + f.entity == 3:
                if field.spaces[f.xPos][f.yPos+1].fighter.hp < selectedHp and field.spaces[f.xPos][f.yPos+1].fighter.hp > 0:
                    selected = 4
                    selectedHp = field.spaces[f.xPos][f.yPos+1].fighter.hp
            if selected == 1:
                field.spaces[f.xPos][f.yPos-1].fighter.hp -= 3
                if field.spaces[f.xPos][f.yPos-1].fighter.hp <= 0:
                    field.spaces[f.xPos][f.yPos-1].entity = 0
                    #fighterdied(f.xPos, f.yPos-1)
            elif selected == 2:
                field.spaces[f.xPos-1][f.yPos].fighter.hp -= 3
                if field.spaces[f.xPos-1][f.yPos].fighter.hp <= 0:
                    field.spaces[f.xPos-1][f.yPos].entity = 0
                    #fighterdied(f.xPos-1, f.yPos)
            elif selected == 3:
                field.spaces[f.xPos+1][f.yPos].fighter.hp -= 3
                if field.spaces[f.xPos+1][f.yPos].fighter.hp <= 0:
                     field.spaces[f.xPos+1][f.yPos].entity = 0
                     #fighterdied(f.xPos+1, f.yPos)
            elif selected == 4:
                field.spaces[f.xPos][f.yPos+1].fighter.hp -= 3
                if field.spaces[f.xPos][f.yPos+1].fighter.hp <= 0:
                     field.spaces[f.xPos][f.yPos+1].entity = 0
                    #fighterdied(f.xPos, f.yPos+1)

            else:

               route = []
               finaldest = (0,0)
               if f.entity == 2:
                   entity = 2
                   for dest in elfDestinations:
                       if dest in distances:
                           dist = distances[dest][0]
                           if dist < minDistance:
                               minDistance = dist
                               route = distances[dest][1:]
                               finaldest = dest
                           elif(dist == minDistance and (dest[1] < finaldest[1] or (dest[1] == finaldest[1] and dest[0] < finaldest[0]))):
                               minDistance = dist
                               route = distances[dest][1:]
                               finaldest = dest
               elif f.entity == 1:
                   entity = 1
                   for dest in goblinDestinations:
                       if dest in distances:
                           dist = distances[dest][0]
                           if (dist < minDistance):                           
                               minDistance = dist
                               route = distances[dest][1:]
                               finaldest = dest
                           elif(dist == minDistance and (dest[1] < finaldest[1] or (dest[1] == finaldest[1] and dest[0] < finaldest[0]))):
                               minDistance = dist
                               route = distances[dest][1:]
                               finaldest = dest

               if len(route) == 0:
                   continue
               moveTo = route[0]
               moveToX = moveTo[0]
               moveToY = moveTo[1]
               oldX = f.xPos
               oldY = f.yPos
              
               #updateAdj((f.xPos, f.yPos), (moveToX, moveToY), entity)
               field.spaces[oldX][oldY].containsEntity = False
               field.spaces[f.xPos][f.yPos].entity = 0
               field.spaces[moveToX][moveToY].entity = entity
               field.spaces[moveToX][moveToY].containsEntity = True
                          
               f.xPos = moveToX
               f.yPos = moveToY

               field.spaces[f.xPos][f.yPos].setFighter(f)
               
               selected = 0
               selectedHp = 1000
               if field.spaces[f.xPos][f.yPos-1].entity + f.entity == 3:
                   if field.spaces[f.xPos][f.yPos-1].fighter.hp > 0:
                       selected = 1
                       selectedHp = field.spaces[f.xPos][f.yPos-1].fighter.hp
               if field.spaces[f.xPos-1][f.yPos].entity + f.entity == 3:
                   if field.spaces[f.xPos-1][f.yPos].fighter.hp < selectedHp and field.spaces[f.xPos-1][f.yPos].fighter.hp > 0:
                       selected = 2
                       selectedHp = field.spaces[f.xPos-1][f.yPos].fighter.hp
               if field.spaces[f.xPos+1][f.yPos].entity + f.entity == 3:
                   if field.spaces[f.xPos+1][f.yPos].fighter.hp < selectedHp and field.spaces[f.xPos+1][f.yPos].fighter.hp > 0:
                       selected = 3
                       selectedHp = field.spaces[f.xPos+1][f.yPos].fighter.hp
               if field.spaces[f.xPos][f.yPos+1].entity + f.entity == 3:
                   if field.spaces[f.xPos][f.yPos+1].fighter.hp < selectedHp and field.spaces[f.xPos][f.yPos+1].fighter.hp > 0:
                       selected = 4
                       selectedHp = field.spaces[f.xPos][f.yPos+1].fighter.hp

               if selected == 1:
                   field.spaces[f.xPos][f.yPos-1].fighter.hp -= 3
                   if field.spaces[f.xPos][f.yPos-1].fighter.hp <= 0:
                       field.spaces[f.xPos][f.yPos-1].entity = 0
                       #fighterdied(f.xPos, f.yPos-1)
               elif selected == 2:
                   field.spaces[f.xPos-1][f.yPos].fighter.hp -= 3
                   if field.spaces[f.xPos-1][f.yPos].fighter.hp <= 0:
                       field.spaces[f.xPos-1][f.yPos].entity = 0
                       #fighterdied(f.xPos-1, f.yPos)
               elif selected == 3:
                   field.spaces[f.xPos+1][f.yPos].fighter.hp -= 3
                   if field.spaces[f.xPos+1][f.yPos].fighter.hp <= 0:
                       field.spaces[f.xPos+1][f.yPos].entity = 0
                       #fighterdied(f.xPos+1, f.yPos)
               elif selected == 4:
                   field.spaces[f.xPos][f.yPos+1].fighter.hp -= 3
                   if field.spaces[f.xPos][f.yPos+1].fighter.hp <= 0:                 
                       field.spaces[f.xPos][f.yPos+1].entity = 0
                       #fighterdied(f.xPos, f.yPos+1)
                   

    elves = 0
    goblins = 0
    totalhp = 0
    fighters = sorted(fighters)
    for f in fighters:
        print("Fighter at: " + str(f.xPos) + ", " + str(f.yPos))
        if f.entity==1 and f.hp>0:
            print("goblin hp: " + str(f.hp))
            totalhp+=f.hp
            goblins+=1
        elif f.entity==2 and f.hp>0:
            print("elf hp: " + str(f.hp))
            totalhp+=f.hp
            elves+=1
    if elves == 0 or goblins == 0:
        print("nr of rounds: " + str(counter))
        print("elves remaining: " + str(elves))
        print("goblins remaining: " + str(goblins))
        print("Hp remaining: " + str(totalhp))
        print("Multiplied: " + str(totalhp*counter))
        break

    counter+=1


