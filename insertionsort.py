# -*- coding: utf-8 -*-
"""
Created on Thu May 29 16:16:12 2025

@author: 996ma
"""

lst=[3,5,2,6,1,7,4]
for i in range(1,len(lst)):
    currentvalue=lst[i]
    correctpostion=i-1
    while(correctpostion>=0):
        if lst[correctpostion]<currentvalue:
            break
        else:
            lst[correctpostion+1]=lst[correctpostion]
            correctpostion-=1
        lst[correctpostion+1]=currentvalue
