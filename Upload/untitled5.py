import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):


    def toPrint(arr):
        for i in arr:
            print(i,end=" ")
        print()
    for j in range(1,n):
        val = arr[j]
        pos = j
        #now run from second last and check for the lowest value else print the list
        for i in range(j-1,-1,-1):
            if arr[i]> val:
                arr[pos] = arr[i]
                pos -= 1
            arr[pos] = val
        toPrint(arr)
    return

            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
