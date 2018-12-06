import re
import operator

file = open("day4data.txt", "r")
data = []
for line in file:
    data.append(line)


dateDict = {'00-00':[-1,[-1,-1],[-1,-1]]}   #GuardID, StartSleepList, StopSleepList
guardDict = {'-1':[[1,],[1,],-1]}  #StartSleepList, StopSleepList, TotalTime Asleep

for line in data:
    if '#' in line:
        guardID = re.search(r'#\d+',line).group()[1:]
        date = line[6:12]      
        time = line[12:17]
        if time[0:3] == '23:':
            month = date[0:2]
            day = date[3:5] 
            if day == '31':
                if month == '12':
                    date = '01-01'
                else:
                    date = date[0] + str(int(date[1])+1) + '-01'
            elif day == '28' and month == '02':
                date = '03-01'
            elif day == '30' and (month == '04' or month == '06' or month == '09' or month == '11'):
                if month == '09':
                    date = '10-01'
                else:
                    date = date[0] + str(int(date[1]) + 1) + '-01'
            elif day == '09':
                date = date[0:3] + '10'
            elif day == '19':
                date = date[0:3] + '20'
            elif day == '29':
                date = date[0:3] + '30'
            else:
                date = date[0:4]+str(int(date[4]) + 1)

        date = date.strip()
        dateDict[date] = [guardID,[0,],[0,]]

for line in data:
    date = line[6:12].strip()    
    time = line[12:17].strip()
    if line[19] == 'f':
        dateDict[date][1].append(int(time[3:]))
    elif line[19] == 'w':
        dateDict[date][2].append(int(time[3:]))
        


for key, value in dateDict.items():
    guardID = value[0]
    startSleepList = value[1]
    stopSleepList = value[2]
    startSleepList.sort()
    stopSleepList.sort()
    for i in range(1,len(startSleepList)):
        startValue = int(startSleepList[i])
        stopValue = int(stopSleepList[i])
        sleepTime = int(stopValue) - int(startValue)
        
        if guardID in guardDict:
            guardDict[guardID][0].append(startValue)
            guardDict[guardID][1].append(stopValue)
            guardDict[guardID][2]+=int(sleepTime)
        else:
            guardDict[guardID] = [[startValue,], [stopValue,], sleepTime]
            
mostAsleepGuard = 0
minutesAsleep = 0

for guard, values in guardDict.items():
    if values[2] > minutesAsleep:
        minutesAsleep = values[2]
        mostAsleepGuard = guard

print(mostAsleepGuard)

minuteMostAsleep = -1
timesAsleep = -1
correspondingGuard = -1

for guard, values in guardDict.items():
   minuteDict = dict()
   minuteDict[-1] = 0
   for i in range(0, len(values[0])):
       start = values[0][i]
       end = values[1][i]
       interval = end - start
       for i in range(0, interval):
           minute = start + i
           if minute in minuteDict:
               minuteDict[minute]+=1
           else:
               minuteDict[minute] = 1

   maxminute = max(minuteDict.items(), key=operator.itemgetter(1))[0]
   if minuteDict[maxminute] > timesAsleep:
       timesAsleep = minuteDict[maxminute]
       minuteMostAsleep = maxminute
       correspondingGuard = guard

print(minuteMostAsleep)
print(correspondingGuard)
print(minuteMostAsleep*int(correspondingGuard))
 
    