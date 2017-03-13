# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:25:04 2017

@author: Peter
"""

import time
import math

def rotate(num, index = 0) :
    assert(type(num) == int)
    if index % len(str(num)) == 0 :
        return num
    else :
        rotate = index % len(str(num))
        listDigit = [i for i in str(num)]
        rotation = listDigit[rotate:] + listDigit[:rotate]
        rotationString = "".join(rotation)
        return int(rotationString)

def rotationList(n) :
    if n == rotate(n, 1) :
        return [n]
    return [rotate(n, i) for i in range(0, len(str(n)))]

def primeBelow(n):
    if n < 2:
        return 0

    listNum = [0, 1, 2] + [i for i in range(3, n, 1)]
    for i in range(2, int(math.sqrt(n)) + 1, 1): 
        if listNum[i] :
            for j in range(i**2, len(listNum), i):
                listNum[j] = 0
    return listNum                   

def main() :
    delta = time.time()
    primeList = primeBelow(1000000)
    count = 0
    pos = 2
    while pos < len(primeList) :
        if primeList[pos] != 0 :
            listRotNum = rotationList(primeList[pos])
            if len(listRotNum) == 1:
                count += 1
            else :  
                circularPrime = True
                for i in range(1, len(listRotNum)) :
                    if listRotNum[i] != primeList[listRotNum[i]] :
                        circularPrime = False
                        break
                if circularPrime :
                    count += 1
        pos += 1   
    delta = time.time() - delta
    return count, delta

print(main())