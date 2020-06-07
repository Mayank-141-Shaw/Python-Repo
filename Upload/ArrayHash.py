# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:00:37 2020

@author: MAYANK SHAW
"""

def VasyaHasher(n, arr, q, lrv):
    result = [0]*q
    for i in range(q):
        #increase the values in range first before finding hash
        l,r,v = lrv[i][0], lrv[i][1], lrv[i][2]
        arCopy = arr
        for j in range(0, len(arCopy)):
            if l<=arCopy[j]<=r:
                arCopy[j] += v
        
        #after increasing we will find hash value on arCopy
        
        while len(arCopy) >= 2:
            arCopyTwo = [0]*(len(arCopy)-1)
            sumval = 0
            sumval = arCopy[1] - arCopy[0]
            arCopyTwo[0] = sumval
            for k in range(2,len(arCopy)):
                arCopyTwo[k-1] = arCopy[k]
            #after copying to new array we will swap the array
            arCopy = arCopyTwo
            #resetting for next run
        
        #if length of arCopy becomes 1
        #we will return the val as vasyahash of the array of q operation
        result[i] = arCopy[0]
    
    return result

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    lrv = [[]]*q
    for i in range(q):
        lrv[i] = list(map(int, input().split()))
    
    result = VasyaHasher(n, a, q, lrv)
    for i in result:
        print(i,end="\n")


if __name__ == '__main__':
    main()
    