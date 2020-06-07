# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:38:18 2020

@author: MAYANK SHAW
"""

#We may use binary search to acquire the target

#the target will move one place to the right if its not hit and wont if its already at the 
# that is the target will spawn randomly at any point or window and start moving right

import random as rd

def MovingTarget(n):
    l,r = 0, n-1
    mid = int((l+r)/2)
    windows = [0]*n
    pos = rd.randint(0,n-1)
    windows[pos] = 1
    #triggers the window
    #now traget will keep moving right with each shot missed
    
    #fingding the target
    hit = 0
    no_of_shots = 1
    result = [hit+1]
    while l<r:
        if pos == hit:
            break
        elif pos == mid:
            windows[mid] = 1
            result.append(mid+1)
            no_of_shots += 1
            break
        elif pos<mid:
            r = mid-1
            pos += 1
            hit = mid
            windows[mid] = 1
            no_of_shots += 1
        else:
            l = mid + 1
            pos += 1
            hit = mid
            windows[mid] = 1
            no_of_shots += 1
    print(no_of_shots)
    print(result)


def main():
    n = int(input())
    MovingTarget(n)
    
if __name__ == '__main__':
    main()