# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:13:47 2017

@author: Peter
"""
import math

LIMITS = 999

MAX_PRIME = 100000

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

def isPrime(n):
    if n > listOfPrimes[len(listOfPrimes) -1]:
        print("ALERT - I did not calculate so many primes ! n is ", n , "my max Prime is ", len(listOfPrimes) -1)
        return False
    if n in listOfPrimes:
        return True
    return False


def numConsecutivePrimes(a,b):
    index = 0
    while (isPrime(index*index+a*index+b)):
        index += 1
    return index

listOfPrimes = generateListOfPrimes(MAX_PRIME)
longestSet = [0,0,0]
for a in range(-LIMITS, LIMITS+1):
    #print(a)
    for b in range(3, LIMITS+1,2): 
        if isPrime(b):
            length = numConsecutivePrimes(a,b)
            if length > longestSet[2]:
                longestSet[0] = a
                longestSet[1] = b
                longestSet[2] = length
                print(longestSet)
    