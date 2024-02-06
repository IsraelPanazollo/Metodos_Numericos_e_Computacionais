# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:19:41 2017

@author: israe
"""

import math

err = 1.0
x0 = 0.0
x1 = -40000000000.0

f = lambda x: x + math.sqrt(x**2+154256400000000000000) - 20000000000000/11398.4

i=0

while err> 0.0001:
    x = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
    err = abs(x-x1)/abs(x)   
   
    x0 = x1
    x1 = x
    i=i+1
    
    print i,("| x=%.9f"%x),err