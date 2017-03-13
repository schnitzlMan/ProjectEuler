# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:39:42 2017

@author: Peter
"""

import math

MAX_PRIME = 1000000

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


# Circularity ! Not ALL permutations
def checkCircularity(i):
    #print("checkCircularity", i)
    iStr = list(str(i))
    #print(iStr)
    #I'm still doing one test too many here...
    for letter in iStr:
        #print(letter)
        popped = iStr.pop(0)
        #print("popped", popped)
        iStr.append(popped)
        #print(iStr)
        rotation = int(''.join(str(x) for x in iStr))
        #print(rotation)
        if (rotation not in primeList):
            #print("this would returns FALSE:", rotation)
            return False
    return True

primeList=generateListOfPrimes(MAX_PRIME)

circularNums = 0
for i in primeList:
    if checkCircularity(i):
        circularNums += 1
        print("found such a value", circularNums, i)
        
        