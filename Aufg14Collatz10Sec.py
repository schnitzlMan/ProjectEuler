import time

checkUpTo = 1000000

iterationsList = [0] * checkUpTo

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

# ist noch immer nicht optimal, ich kann ja noch
# bei jeder Rechnung auch gleich mitspeichern was der Wert für die Elemente
# entlang des Wegs sind. Das macht bestimmt nochmal einen Faktor 2 bis 10 aus


def getCollatzLength(inVal, iterationsList):
    numIterations = 0
    currentVal = inVal
    sequenceKnown = False
    #print(inVal)
    #print(iterationsList)
    if iterationsList[inVal] != 0:
        numIterations = iterationsList[currentVal]
        sequenceKnown = True
    while currentVal != 1 and not sequenceKnown:
        numIterations += 1
        if currentVal%2 == 0:
            currentVal //= 2
        else:
            currentVal = currentVal*3 + 1
        if currentVal < checkUpTo:
            if iterationsList[currentVal] != 0:
                sequenceKnown = True
                numIterations += iterationsList[currentVal]-1
    #print(numIterations+1)
    return numIterations+1 
    

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
        currentLen = getCollatzLength(i, iterationsList)
        iterationsList[i] = currentLen
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


