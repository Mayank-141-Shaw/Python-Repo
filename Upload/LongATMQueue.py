# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:10:56 2020

@author: MAYANK SHAW
"""

def find_groups(n, H):
    checker=[None]
    count = 1
    if n == 0 :
        return 0
    for i in range(n):
        if H[i] not in checker:
            count = count + 1
        else:
            checker.append(H[i])
    return count
    

n = int(input("Enter no.of person:"))
if 1<= n <= 1000000:
    print("Enter values:")
    H=map(input('> ').split())
    print("No. of groups: ",find_groups(n, H))

