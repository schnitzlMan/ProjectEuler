

currentSum = 0
for x in range (0,1000):
    #print("We're on %d", (x))
    if ( x%5 == 0 or  x%3 == 0):
        # print("       and this one fits")
        currentSum += x
print("done the sum is ", currentSum)

## or .. in just one line

# sum([x for x in range(1,1000) if (x%5==0) or (x%3==0)])
