# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 12:08:17 2020

@author: MAYANK SHAW
"""

n = int(input("Enter size of set A:"))
if n<=100 and n>=1:

    A = []
    print("Enter A values")
    for i in range(0,n):
        i = int(input())
        A.append(i)
        
    m = int(input("Enter size of set C:"))
    if m<=100 and m>=1:
        C = []
        print("Enter A values")
        for i in range(0,m):
            i = int(input())
            C.append(i)
            
        B = set()
        
        for i in C:
            for j in A:
                if (i-j not in B):
                    B.add(i-j)
        ls = []
        for i in B:
            for j in A:
                if i+j not in C:
                    ls.append(i)
            
        for i in ls:
            B.remove(i)
        
        print("B: ",B)
    else:
        print("Wrong input size")
else:
    print("Wrong inut size")
