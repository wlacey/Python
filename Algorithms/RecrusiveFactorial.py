# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:52:02 2021

@author: wlacey
"""

def fact(n):
    
    # outputs n
    print(n)
    
    # base case
    if n == 0:
        return 1
    
    else:
        return n * fact(n - 1)
    
# Driver Code
x = fact(4)
print(x)
