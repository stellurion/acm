cases = int(input())

results = []
for c in range(cases):
    output = (input().split(" "))
    output = [int(x) for x in output]
    n, s, m = output

    intervals = [(0, 0)]
    for interval in range(n):
        intervals.append(eval(input().replace(" ", ",")))
    intervals.append((m, m))

    for i in range(len(intervals)-1):
        if s <= (intervals[i+1][0] - intervals[i][1]):
            results.append('yes')
            break

    if len(results) != c+1:
        results.append('no')

for x in results:
    print(x)