# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:08:32 2020

@author: MAYANK SHAW
"""

def hash(key, text):
    sta = list()
    for i,j in key,text:
        sta.append(i+j)
    return sta

k = input("Enter a key: ")
t = input("Enter a text: ")
print(hash(k, t))