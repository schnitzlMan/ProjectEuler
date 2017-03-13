# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 22:00:43 2017

@author: Peter
"""

import math


def deltaToTheLeftOfBottom(n):
    x = (n*n + n - n*math.sqrt(2*n))/ (n*n+1)
    return 1-x

def heightAtN(inVal):
    return (1-deltaToTheLeftOfBottom(inVal))/inVal

def IntegralTriangle(inVal):
    delta = deltaToTheLeftOfBottom(inVal)
    return(delta - .5*delta*math.sqrt(1-delta*delta)- .5*math.asin(delta))

def Numerator(n):
    Delta = IntegralTriangle(n)
    return Delta + .5 * heightAtN(n)*(1-deltaToTheLeftOfBottom(n))

def Denominator(n):
    return 1 - math.pi *0.25
    

for n in range(1,2242):
    print(n, deltaToTheLeftOfBottom(n), heightAtN( n), Numerator(n)/Denominator(n)*100)
    
    