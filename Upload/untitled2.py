# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:11:17 2020

@author: MAYANK SHAW
"""

import re

def ceaserCipher(s, k):
    k=k%26
    out = ''
    asival = 0
    for i in s:
        if i.isalpha() and i.isupper():
            asival = ord(i)
            asival += k
            if asival > ord('Z'):
                asival -= 26
            i = chr(asival)
        elif i.isalpha() and i.islower():
            asival = ord(i)
            asival += k
            if asival > ord('z'):
                asival -= 26
            i = chr(asival)
        out = out + i
    return out

print(ceaserCipher('Hello-how are ! you.', 3))