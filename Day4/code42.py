from datetime import datetime, timedelta


class GuardAction:
    def __init__(self, dateTime, id, action):
        self.dateTime = dateTime
        self.id = id
        self.action = action


class WorkingDay:
    def __init__(self, dateTime, id):
        self.dateTime = dateTime
        self.id = id
        self.timeLine = []
        for i in range(60):
            self.timeLine.append('.')

    def sleep(self, beginTime, wakeUpTime):
        for z in range(beginTime, wakeUpTime):
            self.timeLine[z] = '#'


class Guard:
    def __init__(self, id, startSleepTime):
        self.id = id
        self.totalSleepTime = startSleepTime


f = open("input.txt", "r")

inputList = []

for line in f:
    inputList.append(line.rstrip('\n'))

f.close()

inputList.sort()

guardActionList = []
tempId = ""

for guardAction in inputList:
    action = ""
    firstSplit = guardAction.split('[')
    secondSplit = firstSplit[1].split(']')
    dateTime = datetime.strptime(secondSplit[0], "%Y-%m-%d %H:%M")
    newTime = dateTime
    if dateTime.hour == 23:
        newTime = dateTime + \
            timedelta(minutes=(60 - dateTime.minute))
    thirdSplit = secondSplit[1].split()
    if len(thirdSplit) == 4:
        tempId = thirdSplit[1]
        action = thirdSplit[2]
    else:
        action = thirdSplit[1]
    guardActionList.append(GuardAction(newTime, tempId, action))

workingDayList = []
dayInfo = []

startSleepTime = 0
dayIndex = -1

for guardAction in guardActionList:
    if guardAction.action == "begins":
        dayIndex += 1
        workingDayList.append(WorkingDay(guardAction.dateTime, guardAction.id))
    elif guardAction.action == "asleep":
        startSleepTime = guardAction.dateTime.minute
    else:
        workingDayList[dayIndex].sleep(
            startSleepTime, guardAction.dateTime.minute)

guardlist = []
for day in workingDayList:
    daySleepTime = 0
    for minuteMoment in day.timeLine:
        if minuteMoment == "#":
            daySleepTime += 1
    guardFound = False
    for guard in guardlist:
        if guard.id == day.id:
            guard.totalSleepTime += daySleepTime
            guardFound = True
            break
    if guardFound == False:
        guardlist.append(Guard(day.id, daySleepTime))

highestId = ""
highestHour = 0
highestHourIndex = 0
for guard in guardlist:
    sleepHours = []
    for i in range(60):
        sleepHours.append(0)
    for day in workingDayList:
        if day.id == guard.id:
            for i in range(60):
                if day.timeLine[i] == '#':
                    sleepHours[i] += 1
    for i in range(60):
        if sleepHours[i] > highestHour:
            highestHour = sleepHours[i]
            highestHourIndex = i
            highestId = guard.id
print highestId + "  X  " + str(highestHourIndex) + "  =  " + \
    str(highestHourIndex*int(highestId.split('#')[1]))
