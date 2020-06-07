# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:44:38 2020

@author: MAYANK SHAW
"""

def solve(ar, n, S):
    
    cur_sum = ar[0]
    start = 0
    
    i = 1
    while i<n:
        
        while cur_sum > S and start < i-1:
            cur_sum -= ar[start]
            start += 1
            
        if cur_sum == S:
            print('Subarray is:')
            print(ar[start:i])
            return 1
        
        if i<n:
            cur_sum += ar[i]
        i+=1
    
    print('No subarray')
    return 0

ar = [3,6,2,8,10,4]

solve(ar, len(ar), 13)