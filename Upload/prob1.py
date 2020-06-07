# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:40:00 2020

@author: MAYANK SHAW
"""

import random as rd
import time
def return_heads():
    heads = 0
    for i in range(100):
        if rd.random() <= 0.5:
            heads += 1
    return heads

def generate(n):
    trials = []
    for i in range(0,n):
        trials.append(return_heads())
    for i in range(0,n):
        print("Times occurence of heads : ",trials[i])
        print("Times occurence of tails : ",100-trials[i])
    return trials

a = int(input("Enter no. of times to generate : "))
start = float(time.time())
trial = generate(a)
end = float(time.time())
print("Total time = ",end-start)