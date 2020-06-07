# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:30:50 2020

@author: MAYANK SHAW
"""

def diagonalDifference(arr):
    # Write your code here
    ld,rd = 0,0
    for i in range(len(arr)):
        ld = ld + arr[i][i]
        rd = rd + arr[i][len(arr)-i-1]
    return abs(ld-rd)

n = int(input())
arr = [None]*n
for i in range(n):
    arr[i] = list(map(int, input().split()))
print(diagonalDifference(arr))

