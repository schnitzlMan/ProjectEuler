import time

checkUpTo = 1000000

keepListUpTo = 5 * checkUpTo

iterationsList = [0] * keepListUpTo

def generateCollatz(inVal):
    returnList = [inVal]
    currentVal = inVal
    while currentVal != 1:
        if currentVal%2 == 0:
            currentVal //= 2
        else:
            currentVal = currentVal*3 + 1
        returnList.append(currentVal)
    return returnList


def getCollatzLength(inVal):
    if iterationsList[inVal] != 0:
        return iterationsList[inVal] 

    currentVal = inVal
    sequenceKnown = False
    tempList = []

    while currentVal != 1 and not sequenceKnown:
        tempList.append(currentVal)
        if currentVal%2 == 0:
            currentVal //= 2
        else:
            currentVal = currentVal*3 + 1
        if currentVal < keepListUpTo:
            if iterationsList[currentVal] != 0:
                sequenceKnown = True
        #else:
        #    print('iterationslist exceeded, consider a higher value ', currentVal)

    lengthTempList = len(tempList)
    if lengthTempList > 0:
         for idx, val in enumerate(tempList):
            if val < keepListUpTo:
                iterationsList[val] = lengthTempList - idx + 1 
                if sequenceKnown == True:
                    iterationsList[val] += iterationsList[currentVal] -1 
    return iterationsList[inVal] 
    

# Die Stupide Lösung brauchte 295 sekunden und ergab 837799
def doStupid():
    maxLenFound = 0;
    maxLenIndex = 0;
    for i in range(1,checkUpTo):
        currentLen = len(generateCollatz(i))
        iterationsList[i] = currentLen
        if i%1000 == 0:
            print('index ', i, ' currentLen ', currentLen)
        if currentLen > maxLenFound:
            maxLenFound = currentLen
            maxLenIndex = i
    return maxLenIndex, maxLenFound

# Mit prints bei jedem 1000ten element dauert das 52 s
# komplett ohne prints 12 sec
def doSmart():
    maxLenFound = 0;
    maxLenIndex = 0;
    for i in range(1,checkUpTo):
        # only this function is different compared to DoSmart...
        # this could be arranged better
        currentLen = getCollatzLength(i)
        #print(i)
        #print(generateCollatz(i))
        #print(iterationsList[0:20])
        #iterationsList[i] = currentLen
        #if i%10000 == 0:
        #    print('index ', i, ' currentLen ', currentLen)
        if currentLen > maxLenFound:
            maxLenFound = currentLen
            maxLenIndex = i
    return maxLenIndex, maxLenFound


def solveProblem():
    start_time = time.time()
    maxLenIndex, maxLenFound = doSmart()
    elapsed_time = time.time()-start_time
    print('time used ',elapsed_time)
    print('maxLenIndex ', maxLenIndex, ' maxLenFound ', maxLenFound)
    return

 

solveProblem()


