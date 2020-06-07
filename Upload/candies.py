# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:44:25 2020

@author: MAYANK SHAW
"""
import math as mt

def solve(ar, Q, n, q):
    ct = 0
    for i in range(q):
        operation = Q[i][0]
        if operation=='U':
            #do update operation replacing xth element with v
            ar[int(Q[i][1])] = int(Q[i][2])
        elif operation=='Q':
            #do query operation
            l, r = int(Q[i][1]), int(Q[i][2])
            for j in range(l, r+1):
                ct += (-1)**(j-l) * ar[j] * (j-l+1)
        
    return ct

if __name__=='__main__':
    t = int(input())
    res = []*t
    for i in range(t):
        n, q = map(int, input().split())
        ar = list(map(int, input().split()))
        Q = [[]]*q
        for j in range(q):
            Q[j] = list(map(str, input().split()))
        res[i] = solve(ar, Q, n, q)
        
    for i in range(t):
        print(f'Case #{i+1}: {res[i]}')
