# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:07:32 2021

@author: wlacey
"""

def rev(s):
    # REMEMBER, always need a base case.
    if s == '':
        return s
    
    else:
        print(s)
        return rev(s[1:]) + s[0]

# Driver Code
x = rev('Hello')
print(x)
