cases = int(input())

results = []
for c in range(cases):
    num = int(input())
    results.append(num%10 + int(num/10))

for r in results:
    print(r)