import copy

def backtrack(word, fullword, extra): #full word
    if word == "":
        for f in fullword:
            extra.append(f)
        return fullword
    if len(word) >= 2:
        if validcv(word[0:2]):
            fullwordcopy = copy.deepcopy(fullword)
            fullwordcopy.append(word[0:2])
            if backtrack(word[2:], fullwordcopy, extra) != None: #not saving the pathing correctly
                return fullword
    if len(word) >= 3:
        if validcv(word[0:3]):
            fullwordcopy = copy.deepcopy(fullword)
            fullwordcopy.append(word[0:3])
            if backtrack(word[3:], fullwordcopy, extra) != None:
                return fullword

def validcv(word):
    flag = True

    if word[0] != "b" and word[0] != "c" and word[0] != "d":
        flag = False
    if word[1] != "a" and word[1] != "e":
        flag = False

    return flag

def validcvc(word):
    flag = True

    if word[0] != "b" and word[0] != "c" and word[0] != "d":
        flag = False
    if word[1] != "a" and word[1] != "e":
        flag = False
    if word[2] != "b" and word[2] != "c" and word[2] != "d":
        flag = False

    return flag


lines = int(input())

result = []

for i in range(lines): 
    wordlength = input()
    word = input()
    extra = []
    backtrack(word, [], extra)
    result.append(".".join(extra))

for i in result:
    print(i)

