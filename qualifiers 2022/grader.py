#Kattis MrCodeFormatGrader

def problem():
    first = input().split(' ')
    total_lines = int(first[0]) 
    num_errors = int(first[1]) #i should have used this in hindsight

    line = input().split(' ') #error lines
    line = [eval(i) for i in line]
    invert = list(set(range(1, total_lines+1)) - set(line))

    errors = []
    for pos in clump(line):
        if pos[0] == pos[1]:
            errors.append(str(line[pos[0]]))
        else:
            errors.append(str(line[pos[0]]) + '-' + str(line[pos[1]]))
    correct = []
    for pos in clump(invert):
        if pos[0] == pos[1]:
            correct.append(str(invert[pos[0]]))
        else:
            correct.append(str(invert[pos[0]]) + '-' + str(invert[pos[1]]))

    resulte = 'Errors: '
    for i in errors:
        if i == errors[-1]:
            resulte += str(i)
        elif i == errors[-2]:
            resulte += (str(i) + ' and ')
        else:
            resulte += (str(i) + ', ')
    resultc = 'Correct: '
    for i in correct:
        if i == correct[-1]:
            resultc += str(i)
        elif i == correct[-2]:
            resultc += (str(i) + ' and ')
        else:
            resultc += (str(i) + ', ')

    print(resulte)
    print(resultc)


def clump(line: list):
    clumps = []
    i = 0 #position in list
    while i < len(line):
        start = i

        while i + 1 < len(line) and line[i]+1 == line[i+1]: #create clump
            i += 1
        else:
            end = i

        clumps.append((start, end))
        i += 1

    return clumps

if __name__ == '__main__':
    problem()