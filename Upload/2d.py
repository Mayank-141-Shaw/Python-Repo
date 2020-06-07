#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries, q):
    # Write your code here

    s = [[]]*n
    last_answer = 0
    result = []

    for i in range(q):
        if queries[i][0] == 1:
            x = queries[i][1]
            y = queries[i][2] 
            index = (x ^ last_answer) % n
            print('index:',index)
            s[index][].append(y)
        elif queries[i][0] == 2:
            x = queries[i][1]
            y = queries[i][2]
            index = (x ^ last_answer) % n
            print('index:',index)#this gave us seq list no
            val_index = y%len(s[index])
            print('val_index:',val_index)
            last_answer = s[index][val_index]
            result.append(last_answer)
            
        print(s)
        print()

    return result
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries, q)

    print(result)
