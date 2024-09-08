import math
cases = int(input())

results = []
for case in range(cases):
    x, y, k = input().split(" ")
    x = int(x)
    y = int(y)
    k = int(k)
    xstep = 0 if x == 0 else math.ceil(x/k)
    ystep = 0 if y == 0 else math.ceil(y/k)
    
    parity = 2
    while(xstep >= 0 or ystep >= 0):
        if parity%2 == 0:
            xstep -= 1
        else:
            ystep -= 1
        parity += 1
    results.append(parity-4)

for r in results:
    print(r)

'''
30 
60
90
33
36
39
311

'''