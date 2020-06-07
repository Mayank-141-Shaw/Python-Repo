# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:56:50 2020

@author: MAYANK SHAW
"""

#practice return only prime nmbers

def timeConversion(s):
    TM = s[len(s)-2:]
    time = s[0:len(s)-2]
    hh,mm,ss = map(int,time.split(':'))
    if 1<=hh<=12 and 0<=mm<=59 and 0<=ss<=59:
        if TM == 'PM' and hh!=12:
            hh += 12
        if TM == 'AM' and hh==12:
            hh = 00
    hh,mm,ss = str(format(hh, "02")),str(format(mm, "02")),str(format(ss, "02"))
    return hh+":"+mm+":"+ss
            
    
print(timeConversion("12:45:36AM"))