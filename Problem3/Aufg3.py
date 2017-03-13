
startNum = 600851475143

for i in range(2,(int)(startNum/2)):
    while startNum % i == 0 :
        startNum = startNum / i
        print(i,startNum)
