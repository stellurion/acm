
lines = int(input())

result = []

for i in range(lines):
    one = input()
    two = input()
    three = input()

    matrix = [one, two, three]

    values = []
    for m in matrix: #find values
        if "?"  not in m:
            values = m

    for m in matrix:
        if "?" in m:
            for v in values:
                if v not in m:
                    result.append(v)

for i in result:
    print(i)