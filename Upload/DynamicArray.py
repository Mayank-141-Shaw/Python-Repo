#!/bin/python3

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here

    s = []
    for _ in range(n):
        s.append([])
    last_answer = 0
    result = []

    for i,x,y in queries:
        index = (x ^ last_answer) % n
        if i == 1: 
            s[index].append(y)
        elif i == 2:
              #this gave us seq list no
            val_index = y%len(s[index])
            last_answer = s[index][val_index]
            result.append(last_answer)

    return result

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print(result)