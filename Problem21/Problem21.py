# AmicableNumbers

# in -> num ; out -> sum of devidors
#import math

MAX_NUM = 10000

#crosslimit = math.floor(math.sqrt(MAX_NUM))
#listOfPrimes = []
## now I need a list of primes up to sqrt MAX_NUM
#
#sieve = [False]*(MAX_NUM+1)   # valid indices now from 0 to MAX_NUM
#sieve[0] = True
#sieve[1] = True
#
#for i in range(4,MAX_NUM+1, 2):  # indices and values ar shifted by 1
#    sieve[i] = True
#
#for i in range(3, crosslimit+1, 2):
#    if not sieve[i]:
#        for m in range(i*i, MAX_NUM+1, 2*i):
#            sieve[m] = True
#
#for i in range(2,MAX_NUM):
#    if not sieve[i]:
#        listOfPrimes.append(i)

####################################
# Brutest of all forces anyway;

dVector = [0]  # dVector starts at 0 so dVector[220] will be 284

def sumOfListOfDividors(inVal):
    returnVal = 1
    for j in range(2, int(inVal/2)+1):
        if inVal%j == 0:
            returnVal += j
    return returnVal
            
for i in range(1, MAX_NUM):
    dVector.append(sumOfListOfDividors(i))

sumOfAllPairs = 0
for i in range(1,MAX_NUM):
    if dVector[i] < MAX_NUM:
        if dVector[dVector[i]] == i:
            if i != dVector[i]:
                print(i, dVector[i])
                sumOfAllPairs += i
            
print(sumOfAllPairs)
            
