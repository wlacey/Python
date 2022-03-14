# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:21:21 2021

@author: wlacey
"""

def binary_search(x, nums):
    
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        
        mid = (low + high) // 2
        item = nums[mid]
        
        # shows upper and lower bounds movement during binary search.
        print(f'LOW - {low}')
        print(f'MID - {mid}')
        print(f'HIGH - {high}\n')
        
        if x == item:
            return mid
        
        # x is in lower half of range
        elif x < item:
            # move top marker down
            high = mid - 1
        
        # x is in upper half of range
        else:
            # move bottom marker up
            low = mid + 1
            
    return -1

# Driver code.
ans = binary_search(3, [1,2,3,4,5,6,7,8,9,0])
print(f'Index for x is {ans}.')
