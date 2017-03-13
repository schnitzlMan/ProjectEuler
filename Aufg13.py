
str(sum([int(line.rstrip('\n')) \
               for line in open('C:/Python34/Papa/Euler/Aufg13in.txt')]))[:10]


# read the input
summands = [int(line.rstrip('\n')) for line in open('C:/Python34/Papa/Euler/Aufg13in.txt')]

mySum = 0
for i in range(len(summands)):
    mySum += summands[i]

mySumStr = str(mySum)

print(mySumStr[:10])

print(str(sum([int(line.rstrip('\n')) for line in open('problem13.txt')]))[:10])

