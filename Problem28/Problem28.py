# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:08:51 2017

@author: Peter
"""

diagsum = 1
for i in range(3,1003,2):
    diagsum += 4*i**2-6*i+6
print(diagsum)