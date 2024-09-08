cases = int(input())

results = []
for case in range(cases):
    n, k, q = map(int, input().split())

    array = [int(x) for x in input().split()]
    for query in range(q):
        start, end = map(int, input().split())
        subarray = array[start-1:end]


for r in results:
    print(r)