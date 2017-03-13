

def sumEvenFibosSmallerThan(max):
    smaller = 1
    larger = 1
    curVal = 1
    sum = 0
    while curVal < max :
        curVal = smaller
        temp = larger
        larger = smaller + larger
        smaller = temp
        if (curVal%2 == 0):
            print(curVal)
            sum += curVal
    print(sum)

sumEvenFibosSmallerThan(4000000)
