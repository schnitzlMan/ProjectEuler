# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 22:33:27 2017

@author: Peter
"""

N = 5

#for i in range(2,9**N):
totalSum = 0
for i in range(2,6*9**N):
    ints= [j for j in str(i)]
    thisSum = 0
    for j in ints:
        thisSum += int(j)**N
    if (thisSum == i):
        totalSum += thisSum
        print(i, ints, thisSum)
print(totalSum)