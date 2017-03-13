numMinus1 = 1
#numMinus2 = 1

currentNum = 2
currentIndex = 3

while len(str(currentNum))<1000:
    tempNum = currentNum
    currentNum += numMinus1
    numMinus1 = tempNum
    currentIndex += 1

print(currentIndex, currentNum)
    
