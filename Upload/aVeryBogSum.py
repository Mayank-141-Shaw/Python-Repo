# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:05:42 2020

@author: MAYANK SHAW
"""

def aVeryBigSum(ar):
    s = 0
    for i in range(len(ar)):
        if 0<=ar[i]<=10000000000:
            s += ar[i]
    return s

n = int(input())
if 1<=n<=10:
    arr = list(map(int,input().split()))
    if 1<=len(arr)<=n:
        res = aVeryBigSum(arr)
        print(res)