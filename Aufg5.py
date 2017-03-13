
listOfPrimes = [2, 3, 5, 7, 11, 13, 17, 19]
listOfIntegers = range(20,10,-1)
primesThatFormProduct = {}
currentProduct = 1

def mapOfDividors(inVal):
    returnMap = {}
    for prime in listOfPrimes:
        count = 0
        while inVal%prime ==  0:
            inVal /= prime
            count += 1
        if count > 0:
            returnMap[prime]= (count)
    return returnMap

for i in listOfIntegers:
    print(i)
    currentDividors = mapOfDividors(i)
    print(currentDividors)
    for key in currentDividors:
        if key not in primesThatFormProduct or primesThatFormProduct[key] < currentDividors[key]:
            primesThatFormProduct[key] = currentDividors[key]

for key in primesThatFormProduct:
    currentProduct *= key**primesThatFormProduct[key]

print(currentProduct)
