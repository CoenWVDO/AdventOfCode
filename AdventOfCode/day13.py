
file = open("day13data.txt", "r")
carts= []
map = []

class Cart:
    def __init__(self, xpos, ypos, direction):
        self.pos = [xpos, ypos]
        self.dir = direction
        self.nextI = [[0,1],[-1,0]]
        self.alive = True

    def __eq__(self,other):
        return self.pos == other.pos

    #Comparison needs to happen on y (is pos[1]) first. Only if that is equal, check x
    def __lt__(self,other):
        if self.pos[1] == other.pos[1]:
            return self.pos[0] < other.pos[0]
        else:
            return self.pos[1] < other.pos[1]

    def move(self, map):
        def TwoXTwoMatVecMult(matrix, vector):
            first = matrix[0][0]*vector[0] + matrix[0][1]*vector[1]
            second = matrix[1][0]*vector[0] + matrix[1][1]*vector[1]
            return [first, second]

        if self.alive == False:
            return False

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
            if otherCarts.alive == False:
                continue

            if self.pos[0] == otherCarts.pos[0] and self.pos[1] == otherCarts.pos[1]:
                deleteindex.append(index)
                count+=1
                if count > 1:
                    print("Crash: " + str(self.pos[0]) + ", " + str(self.pos[1]))
                    for i in deleteindex:
                        carts[i].alive = False


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


#part 1/2
while True:
    for cart in carts:     
        cart.move(map)
    alive = 0
    for cart in carts:      
        if cart.alive:
            alive+=1
    if alive == 1:
        for cart in carts:      
            if cart.alive:
                print ("Alive cart at: " + str(cart.pos[0]) + ", " + str(cart.pos[1]))
        break

    carts = sorted(carts)