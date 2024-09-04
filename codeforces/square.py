
lines = int(input())

result = []

for i in range(lines): 
    buckets = input()
    squares = input().split(" ")
    squares = [int(x) for x in squares]

    total = sum(squares)

    if (total ** 0.5).is_integer():
        result.append("yes")
    else:
        result.append("no")

for i in result:
    print(i)