# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:25:23 2020

@author: MAYANK SHAW
"""


def solve(a, n, k):
    
    i, ct = 0, 0
    while i<n:
        trig = True
        if a[i]==k:
            for j in range(i, i+k):
                if a[j] != k-j+i:
                    trig = False
            #even after check if trig is true that is we have sub array
            if trig:
                ct += 1
                i = i+k
            else:
                i += 1
        else:
            i += 1
    return ct

if __name__=='__main__':
    t = int(input())
    res = [0]*t
    for i in range(t):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        res[i] = solve(a, n, k)
    i = 0    
    for a in res:
        print(f'Case #{i+1}: {a}')
        i+=1