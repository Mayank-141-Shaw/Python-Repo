# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 00:25:33 2020

@author: MAYANK SHAW
"""

class ArrayStack:
    _stPoint = -1
    def __init__(self):
        self.stack = list()
        
    def is_empty(self):
        if self._stPoint == -1:
            return True
        else:
            return False
        
    def push(self, val):
        self._stPoint += 1
        self.stack.append(val)
    
    def pop(self):
        if not self.is_empty():
            self._stPoint -= 1
            return self.stack.pop()
    
def check_expr(expr):
    lefty = '({['
    righty = ')}]'
    
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            elif righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

print(check_expr('[{()()}{}]'))