# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:44:22 2020

@author: MAYANK SHAW
"""

def compareTriplets(a, b):
    al,bo = 0,0
    for i in range(len(a)):
        if a[i]<b[i]:
            bo += 1
        elif b[i]<a[i]:
            al += 1
    return [al, bo]

    
a = tuple(map(int, input("Enter Alice values: ").split()))
b = tuple(map(int, input("Enter Bob balues: ").split()))

ans = compareTriplets(a, b)
print(f"{ans[0]} {ans[1]}")