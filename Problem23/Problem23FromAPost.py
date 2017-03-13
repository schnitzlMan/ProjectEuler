# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 09:41:20 2017

@author: Peter
"""

# list divisors
# int -> list

# from a post
# While this is interesting - the code is just as slow as my code is

# 

import time
import math
     
def triMs(t):
    t0 = time.time()
    s = 0
    for i in range(1000000):
        s+=i
    return t/(time.time() -t0)

def listDiv(n):
    l = [1]
    if n > 1: 
        for i in range(2, math.floor(math.sqrt(n))+1):
            if not(n%i):
                l.append(i)
                if not(n//i in l): l.append(n//i)
    return l
def listAbundant(n):
    l = []
    for i in range (1, n+1):
        if sum(listDiv(i)) > i: l.append(i)
    return l
def listBiAbundantSums(n):
    t = time.time()
    l = []
    aList = listAbundant(28123)
    k = 0
    for i in range (1, n + 1):
        k += 1
        if k == 1000:
            k = 0
            print (len(l), i, time.time()-t)
        c = True
        for j in aList:
            if j + 12 > i: break
            if (i - j in aList):
                c = False
                break
        if c: l.append(i)
    return sum(l), triMs(time.time()-t), l
listBiAbundantSums(28123)