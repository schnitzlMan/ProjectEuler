import math


maxPrime = 2000000


def isPrime(inNum):
    if inNum <=1 :
        return False;
    elif inNum < 4 :
        return True;
    elif inNum%2 == 0:
        return False;
    elif inNum < 9:
        return True;
    elif inNum%3 == 0:
        return False;
    else:
        r = math.floor(math.sqrt(inNum))
        f = 5
        while(f<=r):
            if inNum%f == 0:
                return False;
            if inNum%(f+2) == 0:
                return False;
            f=f+6
    return True

def findNextPrime(inPrime):
    # Check whether it is a 6k - 1 or a 6k +1 prime
    isALower = False;
    if (inPrime-1)%6 == 0:
        baseK = (inPrime-1)//6
    elif (inPrime+1)%6 == 0:
        baseK = (inPrime+1)//6
        isALower = True
    else:
        print("incorrect input ", inPrime)

    primeNotFound = True
    if isALower:
        tryThis = 6*baseK + 1
        primeNotFound = not isPrime(tryThis)
    while (primeNotFound):
        baseK += 1
        tryThis = 6*baseK -1
        primeNotFound = not isPrime(tryThis)
        if primeNotFound:
            tryThis += 2
            primeNotFound = not isPrime(tryThis)
    return tryThis

# use [2,3,5,7] manually

lastPrime = 7
sumPrimes = 10
countPrimes = 3

while lastPrime < maxPrime:
    sumPrimes += lastPrime
    countPrimes +=1
    if (countPrimes%1000 == 0 or countPrimes == 10001 ):
        print(countPrimes, lastPrime, sumPrimes)
    lastPrime = findNextPrime(lastPrime)
    
print(countPrimes, lastPrime, sumPrimes)
