import math

limitNumOfDevidors = 500
maxPrime = 100000


#This is still the prime number generator without using better indexing

def generateListOfPrimes(maxPrime):
    print("generating List of Primes \n")
    listOfPrimes = []
    crosslimit = math.floor(math.sqrt(maxPrime))
    sieve = [False]*(maxPrime+1)   # valid indices now from 0 to 100
    sieve[0] = True
    sieve[1] = True

    for i in range(4,maxPrime+1, 2):  # indices and values ar shifted by 1
        sieve[i] = True

    for i in range(3, crosslimit+1, 2):
        if not sieve[i]:
            for m in range(i*i, maxPrime+1, 2*i):
                sieve[m] = True

    for i in range(2, maxPrime+1):
        if not sieve[i]:
            listOfPrimes.append(i)
    print("    done with the list of primes \n")
    return listOfPrimes

# Like problem 5, but better
def mapOfPrimes(inVal,listOfPrimes):
    returnMap = {}
    primeIndex = 0
    currentPrime = listOfPrimes[primeIndex]
    curVal = inVal
    while curVal >= currentPrime:
        countCurrentPrime = 0
        while curVal%currentPrime == 0:
            curVal //= currentPrime
            countCurrentPrime += 1
        if countCurrentPrime > 0:
            returnMap[currentPrime]= countCurrentPrime
        primeIndex += 1
        if primeIndex >= len(listOfPrimes):
            print("List of Primes exceeded, use larger value for maxPrime \n")
            return {}
        else:
            currentPrime = listOfPrimes[primeIndex]
    return returnMap


def appendToListOfDividers(inVal, inList):
    tempList = [ x * inVal for x in inList ]
    # tempList.append(inVal) # 1 war schon in der Liste
    # evtl erst schauen, obs schon in der Liste ist
    tempList += inList
    outList = list(set(tempList))# remove elements that are in the list twice
    return outList

def turnPrimesIntoDeviders(primeMap):
    listOfDividers = [1]
    keysInPrimeMap = len(primeMap)
    for key in primeMap:
        for i in range(primeMap[key]):
            listOfDividers = appendToListOfDividers(int(key), listOfDividers)
    
    return listOfDividers
    

listOfPrimes = generateListOfPrimes(maxPrime)

counter = 0
lastTriangleNum = 0
keepGoing = True
listOfDividers = []

while keepGoing:
    counter += 1
    lastTriangleNum += counter
    dividerMap = mapOfPrimes(lastTriangleNum,listOfPrimes)
    listOfDividers = turnPrimesIntoDeviders(dividerMap)
    #if (counter%100 == 0) :
    #    print("Number ", counter, " TriangleNum ", lastTriangleNum)
    #    #print(dividerMap)
    #    print(sorted(listOfDividers))    
    #    print(len(listOfDividers))
        
    if len(listOfDividers) >= limitNumOfDevidors:
        keepGoing = False
print("Number ", counter, " TriangleNum ", lastTriangleNum)
print(sorted(listOfDividers))    
