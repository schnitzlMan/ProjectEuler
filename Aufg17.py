def numLetters(intVal):
    count = 0
    if intVal == 1000:
        count = 11 #onethousand
        return count
    hunddigit = intVal // 100
    if hunddigit > 0:
        count += 7 # hundred
        count += numLetters(intVal//100)

    if hunddigit > 0 and intVal%100 is not 0:
        count += 3 # and

    # continue with decimals
    intVal = intVal % 100

    # strip of the deci-digit
    decidigit = intVal//10
    #sixty
    #fifty
    #forty
    if decidigit ==6 or decidigit == 5 or decidigit == 4:
        count += 5
    #ninety
    #eighty
    #thirty
    #twenty
    elif decidigit == 9 or decidigit == 8 or decidigit == 3 or decidigit == 2:
        count += 6
    #seventy
    elif decidigit == 7:
        count += 7
    # special treatment for 10 11 12 13 15
    #eleven
    #twelve
    elif intVal == 11 or intVal == 12 :
        count += 6
        intVal  = 0
    #thirteen
    elif intVal == 13:
        count +=8
        intVal = 0
    elif intVal == 10:
    #ten
        count += 3
        intVal = 0
    elif intVal == 15:
    #fifteen
        count +=7
        intVal = 0
    elif intVal == 18:
    #eighteen
        count += 8
        intVal = 0
    elif decidigit == 1:
        count += 4 # teen
        count += numLetters(intVal%10) # six, seven-, ... teen
        intVal = 0
        
    intVal = intVal%10
    # smaller than 10
    if intVal == 1 or intVal == 2 or intVal == 6:
        count += 3
    elif intVal == 3 or intVal == 7 or intVal == 8:
        count +=5 
    elif intVal == 4 or intVal == 5 or intVal == 9:
        count +=4
     
    return count

mySum = 0
for i in range (1, 1001):
    print(i, numLetters(i))
    mySum += numLetters(i)
print(i, mySum)

#incorrect: 69929