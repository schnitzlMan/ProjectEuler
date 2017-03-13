import math

for i in range(1000):
    if (500000-i*1000)%(1000-i) == 0:
        a = i
        b = (500000-1000*i)/(1000-i)
        c = math.sqrt(a*a+b*b)
        print(a,b,c, a*b*c)
