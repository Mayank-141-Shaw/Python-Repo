# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:09:04 2020

@author: MAYANK SHAW
"""
import sys

def miniMaxSum(arr):
    ct = 0
    maxval,minval,maxsum,minsum = 0,sys.maxsize,0,0
    while ct != len(arr):
        for i in range(len(arr)):
            if i != ct:
                maxsum += arr[i]
                minsum += arr[i]
        if maxsum > maxval :
            maxval = maxsum
        if minsum < minval:
            minval = minsum
        ct += 1
        maxsum,minsum = 0,0
    print(f'{minval} {maxval}')
