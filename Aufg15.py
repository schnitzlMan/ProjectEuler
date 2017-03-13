numerator = 1
denominator = 1

for i in range(21,41):
    print(i)
    numerator *= i
for j in range(1,21):
    print(j)
    denominator *= j
print(numerator)

print(numerator / denominator )
