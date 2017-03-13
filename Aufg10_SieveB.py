


# unfinished index arithmetics


import math

limit = 2000000
crosslimit = math.floor(math.sqrt(limit)-1)/2
sieve = [False]*(limit+1)   # valid indices now from 0 to 100
sieve[0] = True
sieve[1] = True

for i in range(4,limit+1, 2):  # indices and values ar shifted by 1
    sieve[i] = True

for i in range(3, crosslimit+1, 2):
    if not sieve[i]:
        for m in range(i*i, limit+1, 2*i):
            sieve[m] = True

sum = 0
for i in range(2, limit+1):
    if not sieve[i]:
        sum += i
        
print(sum)
