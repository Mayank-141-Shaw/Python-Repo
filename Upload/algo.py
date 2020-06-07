# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:40:58 2020

@author: MAYANK SHAW
"""

denominations = [1, 15, 25]

def return_Change(change, denominations):
    
    to_give_back = [0] * len(denominations)
    
    for pos, coin in enumerate(reversed(denominations)):
        while coin <= change:
            change = change - coin
            to_give_back[pos] += 1
    return to_give_back

print(return_Change(30, denominations))