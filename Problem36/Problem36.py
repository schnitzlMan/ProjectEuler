# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 08:23:06 2017

@author: Peter
"""

def isPalindrome(inVal):
    inList = [int(x) for x in str(inVal)]
    
    lengthIn = len(inList)
    for i in range(lengthIn//2):
        #print(" - ", i, lengthIn-1-i) # inList[i], inList[lengthIn-i])
        if inList[i] != inList[lengthIn -1- i]:
            return False
    return True
   
mySum = 0    
for i in range (1,1000000,2):
    if (isPalindrome(i)):
        if (isPalindrome( "{0:b}".format(i))):
            print(i,"{0:b}".format(i))
            mySum += i
    #print(i, bin(i))
print(mySum)    