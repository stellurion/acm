cases = int(input())

results = []
for case in range(cases):
    a, b = input().split(" ")
    a = int(a)
    b = int(b)

    min = (a-a)+(b-a)
    for c in range(a, b+1):
        result = (c-a)+(b-c)
        if result < min:
            min = result

    results.append(min)

for r in results:
    print(r)