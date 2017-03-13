#print(sum(int(digit) for digit in str(2**1000)))

myExpo = 1000
resultStr = str(2**myExpo)
print(sum(list(map(int, resultStr))))
