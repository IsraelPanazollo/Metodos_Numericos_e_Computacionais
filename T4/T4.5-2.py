# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 22:23:05 2017

@author: israe
"""

import numpy as np

x = np.array([0., 0., 0., 0.])
x_ant = np.array([0., 0., 0., 0.])
eps = 0.0001

A = np.array([[-4.064, 2.008, 0., 0.], 
              [1.968, -4.128, 2.032, 0.], 
              [0., 1.928, -4.192, 2.072],     
              [0., 0., 1.872, -4.256]]) 

b = np.array([0., 0., 0., -10.64])


x1 = lambda x2, x3, x4: (b[0] - A[0,1]*x2 - A[0,2]*x3 - A[0,3]*x4)/A[0,0]
x2 = lambda x1, x3, x4: (b[1] - A[1,0]*x1 - A[1,2]*x3 - A[1,3]*x4)/A[1,1]
x3 = lambda x1, x2, x4: (b[2] - A[2,0]*x1 - A[2,1]*x2 - A[2,3]*x4)/A[2,2]
x4 = lambda x1, x2, x3: (b[3] - A[3,0]*x1 - A[3,1]*x2 - A[3,2]*x3)/A[3,3]

err = 10.
while err>eps:
    x[0] = x1(x[1], x[2], x[3])
    x[1] = x2(x[0], x[2], x[3])
    x[2] = x3(x[0], x[1], x[3])
    x[3] = x4(x[0], x[1], x[2])
    err = np.amax(np.absolute(x-x_ant))/np.amax(np.absolute(x))   
    x_ant = np.copy(x)
    
print x,err