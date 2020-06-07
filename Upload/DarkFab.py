# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:40:17 2020

@author: MAYANK SHAW
"""
import math as mt

def DarkFab(arr):
    A, B, n = len(arr[0]), len(arr[1]), int(arr[2])
    Astring ,Bstring = arr[0], arr[1]
    Alen, Blen = A, B
    templen, iter_count = 0, 0
    while templen < n:
        templen = A + B
        A, B = B, templen
        iter_count += 1
    #now we stop because temp length is gretaer or equal to n
    
    #extraction part
    #wwe use ratio trick to get our desired part of the value
    Apart, Bpart, lentogo, indicator = 0, 0, 0, ''
    while templen>Alen and templen>Blen:
        Apart = mt.floor((Alen * templen) / (Alen + Blen))
        Bpart = templen - Apart
        #now we check which part to travrse
        if n <= Apart:
            #we move to Apart
            templen = Apart
            indicator = 'a'
        else:
            templen = Bpart
            lentogo += Apart
            indicator = 'b'
            
    #as we now know which part is required a or b we will extract id 
    #using lentogo as left to right length measure to remember total unnecessary length
    val = " "
    if templen == Alen and indicator == 'a':
        id = n - lentogo
        val = Astring[id-1]
    elif templen == Blen and indicator == 'b':
        id = n - lentogo
        val = Bstring[id-1]
        
    return val

if __name__ == '__main__':
    q = int(input())

    quota = [[]]*q
    for i in range(q):
        quota[i] = list(map(str, input().rstrip().split()))
    
    #now to run them and get result one by one
    result = ['']*q
    for i in range(q):
        result[i] = DarkFab(quota[i])
    
    #printing to stdout
    for i in range(q):
        print(result[i], end="\n")
