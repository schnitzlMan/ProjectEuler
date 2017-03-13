# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:31:46 2017

@author: Peter
"""

# 1.3.2017
# Now this works - however it is still kind of messy.
                           
import math

orderedList = [0,1,2,3,4,5,6,7,8,9]   #the first in Order 
numDigits = len(orderedList)
              
def doPermutations(inInt):
    print("doPermutations", inInt)
    if inInt == 0:
        return orderedList
    if inInt == 1:
        temp = orderedList[numDigits-1]
        orderedList[numDigits-1] = orderedList[numDigits-2]
        orderedList[numDigits-2] = temp
        return orderedList
    for i in range(2,numDigits+1):
        highLimit = math.factorial(i)
        lowLimit = math.factorial(i-1)
        #print("i",i, "highLimit", highLimit, "lowLimit",lowLimit)
        if lowLimit == inInt+1:
            #print("take the last", i-1, "digits and sort them the other way around")
            listOfLastVals = []
            for j in range(numDigits - i +1, numDigits):
                listOfLastVals.append(orderedList[j])
            #print("listOfLastVals",listOfLastVals)
            #print("orderedList", orderedList)
            for i,j in enumerate(range(numDigits -i+1, numDigits)):
                #print(i, j, len(listOfLastVals))
                orderedList[j] = listOfLastVals[len(listOfLastVals)-i-1]
            #print("orderedList", orderedList)  
        elif highLimit == inInt:
            #print("highLimit == inInt = ", inInt)
            #print("take the last ", i-1," digits and put them in inverse order")
            listOfLastVals = []
            for j in range(numDigits - i +1, numDigits):
                listOfLastVals.append(orderedList[j])
            #print(listOfLastVals)
            for k,j in enumerate(range(numDigits - i+1, numDigits)):
                #print(i,k,j)
                orderedList[j] = listOfLastVals[i-2-k]
            #print(orderedList)
            return orderedList
        elif (highLimit > inInt and lowLimit < inInt):
            #print("I found my match!")
            #print("what now...")
            intPart = inInt // lowLimit
            restPart = inInt%lowLimit
            #print("divide inInt by lowLimit gives ", intPart, restPart )         
            #print("in the", i-1,"last digits find the", intPart,"st/nd/rd/th largest")
            listOfLastVals = []
            for j in range(numDigits - i +1, numDigits):
                listOfLastVals.append(orderedList[j])
            #print("listOfLastVals",listOfLastVals)
            #print("so the ",intPart,"largest is", listOfLastVals[intPart-1])
            tempVal = orderedList[numDigits - i]
            #print("replace digit of Index", numDigits - i,"which still holds the value", tempVal, "with", listOfLastVals[intPart-1])
            orderedList[numDigits - i] =  listOfLastVals[intPart-1]
            listOfLastVals[intPart-1] = tempVal
                          
            #print(listOfLastVals)
            listOfLastVals.sort()
            #print("listOfLastVals - sorted", listOfLastVals)
            #print("replace the last digits of orderList and doPermutations of ",restPart) #inInt-intPart*lowLimit)
            for i,j in enumerate(range(numDigits - i+1, numDigits)):
                #print(i,j)
                orderedList[j] = listOfLastVals[i]
            #print(orderedList)
            doPermutations(restPart)
            break

    return orderedList

print(doPermutations(999999))

# yep, returns 2783915460




#for i in range (0,6):
#    orderedList = [0,1,2,3,4,5,6,7,8,9]   #the first in Order 
#    print(i, doPermutations(i))
#   print("------------------------------")
