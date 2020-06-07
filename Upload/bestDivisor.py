# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:36:22 2020

@author: MAYANK SHAW
"""

#!/bin/python3

def sumOfDigits(n):
    dig, s = 0,0
    while(n>0):
        dig = n%10
        s+=dig
        n = n//10
    print(s)
    return s

if __name__ == '__main__':
    n = int(input())
    divisors = []
    lent = int(n/2)
    for i in range(1, lent+1):
        if n%i==0:
            divisors.append(i)
    print(divisors)
    sod_of_n = sumOfDigits(n)
    result = 0
    for i in divisors[::-1]:
        if sumOfDigits(i) >= sod_of_n:
            result = i
            break
            
    if result == 0:
        result = n
    print(result)
    