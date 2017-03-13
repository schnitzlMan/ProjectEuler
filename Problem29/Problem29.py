# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:07:36 2017

@author: Peter
"""


# below is my solution - I saw that 'set' would work out nicely (probably from math)
# then I can always add, but the set only grows if new elements entered.

maxNum = 100
listOfPowers=[]
for i in range(2, maxNum+1):
    for j in range(2,maxNum+1):
        thisVal = i**j
        if not thisVal in listOfPowers:
            listOfPowers.append(thisVal)
            #print(i,j,listOfPowers)
            
print(len(listOfPowers))