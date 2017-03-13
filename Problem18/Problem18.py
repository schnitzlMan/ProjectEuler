f = open('DataInput.txt', 'r')
a = []
for line in f:
    b=line.splitlines()
    a.append(list(map(int,b[0].split()))) # turn those awkward strings into a list of ints
#print(a)

for i,e in reversed(list(enumerate(a))):
    print(i,e, len(e))
    maxInLine = []
    for j in range(len(e)-1):
        a[i-1][j] += max(e[j],e[j+1])
    print(a[i-1])
        