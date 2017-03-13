import re
import string

f = open('p022_names.txt', 'r')
for line in f:
    listOfNames = sorted(re.sub('"','',line).split(",")) 
    
alpha2num = dict(zip(string.ascii_uppercase,range(1, 27) ))

allVal = 0
for i,name in enumerate(listOfNames):
    letterVal = 0
    for letter in name:
        letterVal += alpha2num[letter]
    print(i, name, letterVal )
    allVal += (i+1) * letterVal
              
print(allVal)