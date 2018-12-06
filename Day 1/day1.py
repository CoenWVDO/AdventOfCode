from timeit import default_timer as timer

start = timer()
file = open("data.txt", "r")
data = []

for line in file:
    data.append(int(line))

totalfreq = 0
adict = {0:True,}
done = False

while done == False:
    for integer in data:
        totalfreq+=integer

        if totalfreq in adict:
            print(totalfreq)
            done = True;
            break
        adict[totalfreq] = True

end = timer()
print (end - start)
