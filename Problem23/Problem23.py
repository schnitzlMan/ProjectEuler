import time
import math
from numba import jit

maxNum = 28124

def listOfDividorsDumb(inVal):
    start_time = time.time()
    returnList = []
    for i in range(2, inVal):
        if inVal%i == 0:
            returnList.append(i)
    print("listOfDividorsDumb -time elapsed ", (time.time()-start_time)*1000)
    return returnList

def listOfDividors(inVal):
    #start_time = time.time()
    returnList = [1]
    if inVal == 1:
        return returnList
    r = math.floor(math.sqrt(inVal))
    if r*r == inVal:
        returnList.append(r)
        r = r-1
    f=2
    step= 1
    if inVal%2 != 0: # optimization for odd values
        f = 3
        step = 2
    while f <= r:
        if inVal%f == 0:
            returnList.extend((f,inVal//f))
        f=f+step
    #print("listOfDividors -time elapsed ", time.time(), " ", start_time, " " ,(time.time()-start_time)*1000)
    return returnList
    
def listOfAbundantNumbers():
    print("listOfAbs")
    outList = []
    for i in range(1,maxNum):
        if i < sum(listOfDividors(i)):  # definition of an abundant number
            outList.append(i)
    return outList
  
listAb=listOfAbundantNumbers()    

@jit
def isValSumOfTwoAbundants(inVal):
    for i in range(len(listAb)):
        #print(inVal, i, listAb[i])
        if listAb[i] > inVal:
            #print("listAb[i] > inVal - escape")
            return False
        #partnerVal = inVal - listAb[i]
        #for j in range(i,len(listAb)):
        #    if listAb[j] > partnerVal:
        #        #print(inVal, i, j, listAb[i], listAb[j])
        #        break
        #    elif listAb[j] == partnerVal:
        #        return True
            
        if (inVal - listAb[i]) in listAb:
            #print("value found - escape")
            #print (inVal, listAb[i], inVal-listAb[i])
            return True
    return False


### THIS IS WAY TO SLOW - I DON'T KNOW WHY ???


sumVals = 0
for i in range(maxNum):
    #print(i)
    if isValSumOfTwoAbundants(i) == False: 
        sumVals += i
print(sumVals)