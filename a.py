# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 18:07:51 2016

@author: aa
"""
import numpy as np
from scipy import linalg
p=100
def f_a():
    return p
    
A=np.array([[3,2,0],[1,-1,0],[0,5,1]])
b=np.array([[2,4,-1],[3,2,0],[1,0,2]])
x=linalg.solve(A,b.T)
det=np.linalg.det(A)


S=np.zeros((3,3))
f=np.zeros((1,3))