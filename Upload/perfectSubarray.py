# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:57:16 2020

@author: MAYANK SHAW
"""

import math
def isPerfect(k):
    # take out the square root annnd if its a whole number
    krt = math.sqrt(k)
    if k == 0:
        return True
    if krt.is_integer():
        return True
    return False

def perfectSubarray(ar, n):
    ''' We take i=0 and j=n-1 and run i till n/2 position'''
    ct = 0
    S = 0
    i = 0
    j = n-1
    while i<j:
        # first we take total sum
        S = sum(ar[i:j+1])
        if isPerfect(S):
            ct += 1
        S = 0
        
        #now we check for i and j position individuals
        if isPerfect(ar[i]):
            ct += 1
        if isPerfect(ar[j]):
            ct += 1
            
        #now we take 1 less from last ie j-1
        if j>i:
            S = sum(ar[i:j])
            if isPerfect(S):
                ct += 1
        S = 0
        
        #now we take 1 plus from front ie i+1
        if i<j:
            S = sum(ar[i+1:j+1])
            if isPerfect(S):
                ct += 1
        S = 0
        
        #now we move ahead in loop
        i = i+1
        j = j-1
        
    # for odd length of array
    if i == j and isPerfect(ar[i]):
        ct += 1
    
    return ct



if __name__=='__main__':
    t = int(input())
    
    results = [0]*t
    
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        
        results[i] = perfectSubarray(ar, n)
        
    for i in range(t):
        print(f'Case {i+1}: ',results[i])