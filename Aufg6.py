
totalSum = 0
for i in range (101):
    print(i)
    for j in range(i):
        totalSum += i*j

totalSum *=2

print(totalSum)
