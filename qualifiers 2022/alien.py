#failed

def problem():
    num = int(input())

    result = ''
    unique = set([int(x) for x in str(num)]) #or you can do set(str(num).split())

    if unique == {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}:
        print('Impossible')
    else:
        #iterate down
        for i in range (num-1, -1, -1):
            if match(i, unique):
                result = i
                break

        #iterate up
        iterate = num+1
        for i in range(0, num-result): #if any bigger, won't be needed as it ain't close
            if match(iterate, unique):
                if i != num-result-1: #if equals, both are added
                    result = iterate
                else:
                    result = str(result) + ' ' + str(iterate)
                break

            iterate = iterate+1

        print(result)


def match(num: int, unique: set):
    listing = [int(x) for x in str(num)]
    
    if set(listing) & unique == set():
        return True
    else:
        return False

if __name__ == '__main__':
    problem()