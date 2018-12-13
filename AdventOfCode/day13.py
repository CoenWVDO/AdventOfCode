
file = open("test2.txt", "r")



carts= []
map = []

crashlocation = []

class Cart:
    def __init__(self, xpos, ypos, direction):
        self.pos = [xpos, ypos]
        self.dir = direction
        self.nextI = [[0,1],[-1,0]]

    def __eq__(self,other):
        return self.pos == other.pos

    def __lt__(self,other):
        if self.pos[0] == other.pos[0]:
            return self.pos[1] < other.pos[1]
        else:
            return self.pos[0] < other.pos[0]

    def move(self, map):
        def TwoXTwoMatVecMult(matrix, vector):
            first = matrix[0][0]*vector[0] + matrix[0][1]*vector[1]
            second = matrix[1][0]*vector[0] + matrix[1][1]*vector[1]
            return [first, second]

        self.pos[0]+=self.dir[0]
        self.pos[1]+=self.dir[1]
        moveto = map[self.pos[1]][self.pos[0]]
        if moveto == '+':
            self.dir = TwoXTwoMatVecMult(self.nextI,self.dir)
            if self.nextI == [[0,1],[-1,0]]:
                self.nextI = [[1,0],[0,1]]
            elif self.nextI == [[1,0],[0,1]]:
                self.nextI = [[0,-1],[1,0]]
            else:
                self.nextI = [[0,1],[-1,0]]
        elif moveto == '/':
            self.dir = TwoXTwoMatVecMult([[0,-1],[-1,0]], self.dir)
        elif moveto == "\\":
            self.dir = TwoXTwoMatVecMult([[0,1],[1,0]], self.dir)

        count = 0
        deleteindex = []
        for index, otherCarts in enumerate(carts):           
            if self.pos[0] == otherCarts.pos[0] and self.pos[1] == otherCarts.pos[1]:
                deleteindex.append(index)
                count+=1
                if count > 1:
                    print("Crash: " + str(self.pos[0]) + ", " + str(self.pos[1]))
                    deleteindex = reversed(deleteindex)
                    for i in deleteindex:
                        carts.pop(i)
                    return True                    
        return False

def findOccurrences(st, character):
    return [i for i, letter in enumerate(st) if letter == character]

#Find and initialize all carts
y = 0
for line in file:
    map.append([])
    for i in line:
        map[y].append(i)
    cartsFacingLeft = findOccurrences(line, '<')
    cartsFacingRight = findOccurrences(line, '>')
    cartsFacingUp = findOccurrences(line, '^')
    cartsFacingDown = findOccurrences(line, 'v')
    for car in cartsFacingLeft:
        map[y][car] = '-' 
        cart = Cart(car, y, [-1,0])
        carts.append(cart)
    for car in cartsFacingRight:
        map[y][car] = '-' 
        cart = Cart(car, y, [1,0])
        carts.append(cart)
    for car in cartsFacingUp:
        map[y][car] = '|' 
        cart = Cart(car, y, [0,-1])
        carts.append(cart)
    for car in cartsFacingDown:
        map[y][car] = '|' 
        cart = Cart(car, y, [0,1])
        carts.append(cart)
    y+=1


count = 0
drawmap = []

import copy
check = 0
collided = False

while collided == False:
    #This deepcopy was used for drawing (to check the example) but takes up huge chunks of memory
    #drawmap = copy.deepcopy(map)
    count+=1
    if check == 1:
        collided = True
    for cart in carts:        
        cart.move(map)
        if len(carts) == 1:
            check = 1

    if collided :
        print("Last cart at: " + str(carts[0].pos[0]) + ", " + str(carts[0].pos[1]))
    carts = sorted(carts)