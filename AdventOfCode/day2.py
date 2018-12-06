from timeit import default_timer as timer
start = timer()
file = open("day2data.txt", "r")
dat = []
for line in file:
    dat.append(line)

nrOfTwo = 0
nrOfThree = 0

dic = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0,
          'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 
          'o':0, 'p':0,'q':0, 'r':0, 's':0, 't':0,'u':0, 
          'v':0, 'w':0, 'x':0, 'y':0, 'z':0, '\n':0}

for line in dat:
    two = False
    three = False
    for character in line:
            dic[character]+=1
    for key in dic:
        if dic[key] == 2:
            two = True
        elif dic[key] == 3:
            three = True
        dic[key] = 0
    if two:
        nrOfTwo+=1
    if three:
        nrOfThree+=1
    
print(nrOfTwo*nrOfThree)
end = timer()
print ("Time passed: " + str(end-start))

#part 2:

start = timer()
done = False

for index, box in enumerate(dat):
    if done:
        break
    for box2 in dat[index:]:
        differences = [i for i in range(len(box) - 1) if box[i] != box2[i]]
        if len(differences) == 1:
            f = open("output.txt", "w")
            printbox = box2[0:differences[0]] + box2[differences[0]+1:len(box2)-1]
            f.write(printbox)
            f.close()
            print(printbox)
            print(differences[0])
            done = True
            break


end = timer()
print(end - start)