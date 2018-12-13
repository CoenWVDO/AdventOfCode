
import re

file = open("day12data.txt", "r")
data = []
datastring = ""
for line in file:
        data.append(line.strip('\n'))
        datastring+=line
plantState = 400*"." + data[0][15:] + 400*"."

#replace . by n because . messes up regex expression
datastring = datastring.replace(".","n")
plantState = plantState.replace(".","n")

#Part 2 (part 1 removed): check 0-300 generations and try to find a pattern
for j in range(0,300):
    nextState = ['n' for x in range(0,len(plantState))]
    for index, pot in enumerate(nextState):
        potSurroundings = plantState[index-2:index+3]
        if len(potSurroundings) < 5:
            continue
        my_regex = r"" + potSurroundings + "\s=>\s#"
        if re.search(my_regex, datastring):
            nextState[index] = '#'

    plantState = "".join(nextState)


    potSum = 0
    for index, value in enumerate(plantState):
        if value == '#':
            potSum+=(index-400)

    print ("Potsum for " + str(j + 1) + " generations: " + str(potSum))


#from 100 generations, 50 is added each cycle
#after 100 gens the potSum is 6225
#so after 50000000000 generations, the potSum is:

print (6175 + (50000000000 - 100)*50)