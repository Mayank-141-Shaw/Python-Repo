# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:59:10 2020

@author: MAYANK SHAW
"""



def superReducedString(s):
    
    def checkDoubles(st):
        for i in range(len(st)):
            if i+1 != len(st):
                if st[i] == st[i+1]:
                    return True
        return False
    
    def returnIndex(s):
        for i in range(len(s)):
            if i+1 != len(s):
                if s[i]==s[i+1]:
                    return i
    
    if s=="":
        return 'Empty String'
    sval = ''
    while True:
        i = 0
        if checkDoubles(s):
            i = returnIndex(s)
            sval = s[0:i]+s[i+2:len(s)]
            s = sval
            sval = ''
        else:
            if s=="":
                return 'Empty String'
            else:
                return s
    
s= "aaaabbbbccccdddd"
result = superReducedString(s)
print(result)