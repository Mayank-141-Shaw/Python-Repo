# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:47:00 2020

@author: MAYANK SHAW
"""

def hackerrankInString(s):
    def returnPointer(s, char_to_search, start_index):
        ptr = start_index
        while ptr < len(s):
            if s[ptr] == char_to_search:
                return ptr
            ptr += 1
        return -1
    
    check_array = "hackerrank"
    n = len(check_array)
    pointer_array = [0]*n
    ptr = pointer_array[0]
    for i in range(n):
        ptr = returnPointer(s, check_array[i], ptr)
        pointer_array[i] = ptr
        ptr += 1        # must be the next index position
    
    for pos in pointer_array:
        if pos == -1:
            return 'NO'
    return 'YES'

print(hackerrankInString('hackerworld'))
