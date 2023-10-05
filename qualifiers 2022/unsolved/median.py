#time limit exceeded

def problem():
    num = int(input())

    result = []
    for i in range(num): #number of cases
        total = 0

        length = int(input())
        listing = input().split(' ')
        ints = [eval(i) for i in listing]

        for i in range (1, length+1):
            work = ints[:i] #incremented list

            sorty = sorted(work)
            middle = len(sorty)//2

            if len(sorty) % 2 != 0:
                median = sorty[middle]
            else:
                median = (sorty[middle] + sorty[middle-1]) // 2

            total += median

        result.append(total)

    for i in result:
        print(i)

if __name__ == '__main__':
    problem()