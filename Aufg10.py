
maxInt = 2000000
listOfPrimes = [2,3,5]
sumOfPrimes = 10

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
while listOfPrimes[-1] <  maxInt:
    if not findDivisor(valToCheck):
        if valToCheck > maxInt:
            break
        listOfPrimes.append(valToCheck)
        sumOfPrimes += valToCheck
        if len(listOfPrimes)%100 == 0:
            print(len(listOfPrimes), valToCheck, sumOfPrimes)
    valToCheck +=2
print(len(listOfPrimes), valToCheck, sumOfPrimes)

