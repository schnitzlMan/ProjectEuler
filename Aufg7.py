
goal = 100001

listOfPrimes = [2,3,5]

def findDivisor(valToCheck):
    divisorFound = False
    for i in listOfPrimes:
        if valToCheck%i == 0:
            divisorFound = True
            break
    return divisorFound

# here is a lot of improvement to be made...
# but it works for the moment

valToCheck = listOfPrimes[-1] + 2
while len(listOfPrimes) <  goal:
    if not findDivisor(valToCheck):
        listOfPrimes.append(valToCheck)
        if (len(listOfPrimes)%100 == 0):
            print(len(listOfPrimes), valToCheck)
    valToCheck +=2

