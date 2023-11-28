#time limit exceeded

import math

def problem():
    first = input().split(' ') #c = max    n = # of farms with at least 1 cow    m = day when reg visits  #cows in each farm on day0
    c = int(first[0])
    n = int(first[1])
    m = int(first[2])

    farms = []
    for i in range (n): #farms
        farms.append(int(input()))

    days = []
    for i in range (m): #days
        days.append(int(input()))

    inspect = []
    for day in days:
        current = farms[::]

        for i in range(-1, day):
            #morning split
            for farm in range(len(current)):
                if current[farm] > c:
                    split = current[farm]
                    current[farm] = math.ceil(split/2)
                    current.append(math.floor(split/2))

            #end of day, double
            for farm in range(len(current)):
                current[farm] *= 2

        inspect.append(len(current))

    for i in inspect:
        print(i)

if __name__ == '__main__':
    problem()