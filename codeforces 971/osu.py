cases = int(input())

results = []
for c in range(cases):
    rows = int(input())
    order = []
    for r in range(rows):
        line = input()
        order.insert(0, line.index('#')+1)
    results.append(" ".join(str(x) for x in order))

for r in results:
    print(r)