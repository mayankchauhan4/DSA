# -*- coding: utf-8 -*-
"""
Created on Thu May 29 15:28:50 2025

@author: 996ma
"""
lst=[3,5,2,6,1,7,4]
def bubble_sort(lst):
    # Your code goes here
    for i in range(len(lst)-1):
        print(i)
        for j in range(0,len(lst)-i):
            print(len(lst)-i-1)
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

bubble_sort(lst)
