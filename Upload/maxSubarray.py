# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:26:26 2020

@author: MAYANK SHAW
"""

from sys import maxsize

def solveSubarray(ar, n):
    
    max_so_far = -maxsize-1
    max_ended_here = 0
    
    for i in range(0,n):
        
        max_ended_here += ar[i]
        if max_so_far < max_ended_here:
            max_so_far = max_ended_here
            
        if max_ended_here < 0:
            max_ended_here = 0
    return max_so_far

print(solveSubarray([-2,-3, 4,0,-1,-2,5,7,-3], 9))