# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:23:07 2020

@author: MAYANK SHAW
"""

#!/bin/python3

import math
#
# Complete the movingTiles function below.
#
def movingTiles(l, s1, s2, queries):
    #
    # Write your code here.
    #
    #area of qi is product of diagonalls of qi
    #thtat is we need to find 
    result = []
    for qi in queries:
        Lh = l - math.sqrt(qi)
        Sh = math.fabs(s1 - s2)/ math.sqrt(2)
        result.append(Lh/Sh)
    return result

if __name__ == '__main__':

    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    print('\n'.join(map(str, result)))
    print('\n')

