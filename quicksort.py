# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 20:55:52 2016

@author: aa
"""
import random
import copy
def quickSort(L, low, high):
    i = low 
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1                                                             
        L[i] = L[j]
        while i < j and L[i] <= key:    
            i = i+1 
        L[j] = L[i]
    L[i] = key 
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L
#L=[5,0,4,6,8,7,1,3,4,6,12,4,654,354,4,5,7,6,9,6,6,54,7,3,8]
Lold=[random.random() for i in range(10000)]
L=copy.copy(Lold)
Lnew=quickSort(L, 0, len(L)-1)