# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:53:35 2020

@author: MAYANK SHAW
"""


def checkPassStrength(s):
    #set counters
    sp_chars = "!@#$%^&*()-+"
    slflag,clflag,digflag,spflag,lenflag = 1,1,1,1,1
    count = 0
    flag_count = 0
    if len(s) >= 6:
        lenflag = 0
        for i in s:
            if i.islower():
                slflag = 0
            elif i.isupper():
                clflag = 0
            elif i.isdigit():
                digflag = 0
            elif i in sp_chars:
                spflag = 0
    else:
        count = 6-len(s)
        for i in s:
            if i.islower():
                slflag = 0
            elif i.isupper():
                clflag = 0
            elif i.isdigit():
                digflag = 0
            elif i in sp_chars:
                spflag = 0
    
    if slflag == 1:
        flag_count += slflag
    if clflag == 1:
        flag_count += clflag
    if digflag == 1:
        flag_count += digflag
    if spflag == 1:
        flag_count += spflag

    if count >= flag_count:
        return count
    else:
        return flag_count

def main():
    out_int = 0
    s = "Ab1$h"
    
    out_int = checkPassStrength(s)
    
    print(out_int)
    
if __name__ == '__main__':
    main()