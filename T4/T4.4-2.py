# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 16:49:50 2017

@author: israe
"""

import numpy as np

x = np.array([0., 0., 0., 0., 0.])
x_ant = np.array([0., 0., 0., 0., 0.])
eps = 0.001

A = np.array([[6.1, 0.32, 1.3, 2.1, 0.11], 
              [0.82, 8.81, 1.01, 3., 3.12], 
              [0.5, 1.78, 15.2, 4.2, 8.1],     
              [4.2, 5.3, 1.8, 20.9, 7.51],     
              [0.2, 9.1, 4.68, 4.3, 20.1]]) 

b = np.array([19.52, 15.83, -22.14, 27.28, -21.78])

x1 = lambda x2, x3, x4, x5: (b[0] - A[0,1]*x2 - A[0,2]*x3 - A[0,3]*x4 - A[0,4]*x5)/A[0,0]
x2 = lambda x1, x3, x4, x5: (b[1] - A[1,0]*x1 - A[1,2]*x3 - A[1,3]*x4 - A[1,4]*x5)/A[1,1]
x3 = lambda x1, x2, x4, x5: (b[2] - A[2,0]*x1 - A[2,1]*x2 - A[2,3]*x4 - A[2,4]*x5)/A[2,2]
x4 = lambda x1, x2, x3, x5: (b[3] - A[3,0]*x1 - A[3,1]*x2 - A[3,2]*x3 - A[3,4]*x5)/A[3,3]
x5 = lambda x1, x2, x3, x4: (b[4] - A[4,0]*x1 - A[4,1]*x2 - A[4,2]*x3 - A[4,3]*x4)/A[4,4]

err = 10.
while err>eps:
    x[0] = x1(x[1], x[2], x[3], x[4])
    x[1] = x2(x[0], x[2], x[3], x[4])
    x[2] = x3(x[0], x[1], x[3], x[4])
    x[3] = x4(x[0], x[1], x[2], x[4])
    x[4] = x5(x[0], x[1], x[2], x[3])    
    err = np.amax(np.absolute(x-x_ant))/np.amax(np.absolute(x))   
    x_ant = np.copy(x)
    
print x,err


