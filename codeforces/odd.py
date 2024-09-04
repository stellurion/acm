
lines = int(input())

result = []

for i in range(lines):
    var = input().split(" ")
    if var[0] == var[1]:
        result.append(var[2])
    if var[0] == var[2]:
        result.append(var[1])
    if var[1] == var[2]:
        result.append(var[0])

for i in result:
    print(i)