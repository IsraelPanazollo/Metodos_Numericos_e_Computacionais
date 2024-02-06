# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:30:06 2017

@author: israe
"""

import math

f = lambda x: 1.24 - 0.5*math.pi + math.asin(x)+ x*math.sqrt(1-x**2) 
df = lambda x: 2*math.sqrt(1-x**2)

x0 = 0.4
eps = 0.00001

err = 10.0
x_ant = x0
i = 0

while err>eps:
    x = x_ant-f(x_ant)/df(x_ant)    
    err = abs(x-x_ant)
    x_ant = x
    i=i+1
    print i, "| x=%.9f"%x, "| err=%.9f"%err
   