# -*- coding: utf-8 -*-
"""
Created on Sun May 25 17:27:53 2025

@author: 996mayank
"""
letters=['c','f','j']
target='k'

def binserch(letters,target):
    start=0
    end=len(letters)-1
    while(start<=end):
        mid=(start+end)//2
        if (letters[mid]==target):
            return letters[mid+1]
        elif (letters[mid]>target):
            end=mid-1
        elif (letters[mid]<target):
            start=mid+1
    return letters[0]
    
    
binserch(letters,target)
