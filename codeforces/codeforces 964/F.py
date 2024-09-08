from itertools import combinations
cases = int(input())

results = []
for c in range(cases):
    output = (input().split(" "))
    output = [int(x) for x in output]
    n, k = output
    array = list(eval(input().replace(" ", ",")))

    subsequences = list(combinations(array, k))

    medians = []
    for s in subsequences:
        medians.append(sorted(s)[k//2])

    print(sum(medians))