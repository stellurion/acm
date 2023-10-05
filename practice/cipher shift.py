#codeforces 1840A

def test():
    problems = int(input())

    results = []
    for i in range(problems):
        final = ""
        length = int(input())
        latin = input()

        while(latin != ""):
            front = latin[0] #find front
            latin = latin[1:] #remove front
            end = latin.find(front) #find end

            final += front #add chara
            latin = latin[end+1:] #concat latin
        results.append(final) #add result

    for i in results:
        print(i)

test()