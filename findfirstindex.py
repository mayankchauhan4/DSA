# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 21:28:28 2025

@author: Mayank Chauhan
"""

def firstindex(l1,x):
    if (len(l1)==0):
        return -1
    if (l1[0]==x):
        return 0
    ans=firstindex(l1[1:],x)
    print(ans)
    if(ans==-1):
        return ans
    else:
        return ans+1
print(firstindex([3,2,4,3,2,1],1))