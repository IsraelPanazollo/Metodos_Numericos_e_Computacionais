# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 22:51:36 2017

@author: israe
"""


import numpy as np

x = np.array([0., 0., 0.])
x_ant = np.array([0., 0., 0.])
eps = 0.001

A = np.array([[-10., 2., 2.], 
              [1., 6., 0.], 
              [1., 1., 3.]]) 

b = np.array([-8., 7., 0.])


x1 = lambda x2, x3: (b[0] - A[0,1]*x2 - A[0,2]*x3)/A[0,0]
x2 = lambda x1, x3: (b[1] - A[1,0]*x1 - A[1,2]*x3)/A[1,1]
x3 = lambda x1, x2: (b[2] - A[2,0]*x1 - A[2,1]*x2)/A[2,2]

err = 10.
while err>eps:
    x[0] = x1(x[1], x[2])
    x[1] = x2(x[0], x[2])
    x[2] = x3(x[0], x[1])
    err = np.amax(np.absolute(x-x_ant))/np.amax(np.absolute(x))   
    print "maior valor x", np.max(np.absolute(x))  
    print "maior valor x_ant",np.max(np.absolute(x_ant))
    print "erro", err
    x_ant = np.copy(x)
    
print x,err