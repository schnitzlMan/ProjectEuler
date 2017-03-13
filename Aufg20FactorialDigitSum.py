def factorial(inVal):
    prod = 1
    for i in range(1, inVal+1):
        prod *= i
    return prod
        


print(sum(int(digit) for digit in str(factorial(100))))
