import sys
cases = int(input())

results = []
for case in range(cases):
    n, k = (input()).split(" ")
    n = int(n)
    k = int(k)

    array = [k+x for x in range(n)]
    total = sum(array) #can be done instead with the arithmetic sum

    min = float('inf')
    for i in range(n):
        left = sum(array[0:i])
        result = abs(left + -(total-left))

        if result < min:
            min = result
        else:
            break

        
    results.append(min)

for r in results:
    print(r)