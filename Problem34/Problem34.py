# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:42:50 2017

@author: Peter
"""

import math
import time

#for i in range(2,9**N):
initial=time.time()
totalSum = 0
for i in range(10,10000000):
    ints= [j for j in str(i)]
    thisSum = 0
    for j in ints:
        thisSum += math.factorial(int(j))
    if (thisSum == i):
        totalSum += thisSum
        print(i, ints, thisSum)
print(totalSum)
elapsed=time.time()-initial
print('time elapsed: ', elapsed)