#automatic control machine 
#time limit exceeded


import itertools
import functools
import operator


def problem():
    machines  = int(input())

    #check wth all the sets first, whichever has the most overlap put it in first
    all = []

    for i in range (machines):
        first = input().split()
        m = int(first[0])
        n = int(first[1])

        goal = tuple([1]*m)

        matrix = [[0 for x in range(m)] for y in range(n)] 
        for x in range(n):
            row = list(input())
            for y in range(m):
                matrix[x][y] = int(row[y])
        
        result = -1
        combos = []   
        for x in range(n+1):
            for subset in itertools.combinations(matrix, x):
                if summ(subset, m) == goal:
                    size = len(subset)
                    if(result < 0):
                        result = size
                    elif(size < result):
                        result = size

        all.append(result)
    for a in all:
        print(a)

def summ(combo):
    return list(map(operator.add, combo))

print(zip([1, 2, 3], [2, 3, 4], [3, 4, 5]))


# def summ(combo, m):
#     slay = [0] * m

#     for i in range(len(combo)):
#         slay = add(slay, combo[i])

#     return tuple(slay)
        
def add(one, two):
    result = []
    for i in range(len(one)):
        if(one[i] + two[i] > 1):
            result.append(1)
        else:
            result.append(one[i] + two[i])
    return result

if __name__ == '__main__':
    problem()