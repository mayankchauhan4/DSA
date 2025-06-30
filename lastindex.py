# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 21:29:11 2025

@author: Mayank Chauhan
"""

def last_index_recursive(arr, target, index=None):
   
    if index is None:
        index = len(arr) - 1  # Start from the last element

    # Base case: If we've gone through the entire list without finding the element
    if index < 0:
        return -1

    # If the current element matches the target, return its index
    if arr[index] == target:
        return index
    else:
        # Otherwise, recursively call with the previous index
        return last_index_recursive(arr, target, index - 1)
    
    

print(last_index_recursive([3,2,4,3,2,1],2))

