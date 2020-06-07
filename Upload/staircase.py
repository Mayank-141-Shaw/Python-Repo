# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:09:35 2020

@author: MAYANK SHAW
"""

def staircase(n):
    if 0<n<=100:
        for i in range(n,0,-1):
            for j in range(1,n+1):
                if j < i:
                    print(' ',end="")
                else:
                    print('#',end="")
            print()

staircase(6)