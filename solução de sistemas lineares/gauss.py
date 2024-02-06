# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:33:55 2017

@author: buriol
"""
import numpy as np

M = np.array([[3.,0.,1.,1.],
              [3.,2.,1.,1.],
              [-3.,1.,3.,3.]])

# Pega o numero de linhas de M
n = len(M)
#print (n)

for j in range(n):
    for i in range(j,n-1):
        m = M[i+1,j]/M[j,j]
        M[i+1] = M[i+1]-m*M[j]

print (M)

