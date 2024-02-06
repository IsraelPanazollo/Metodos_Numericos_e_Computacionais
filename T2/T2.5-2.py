# -*- coding: utf-8 -*-
"""
Created on Sun Oct 01 15:33:13 2017

@author: israe
"""

import math

f = lambda x: x + math.sqrt(x**2+154256400000000000000) - 20000000000000/11398.4
df = lambda x: 1+ x/math.sqrt(x**2+154256400000000000000)

x0 = -40000000000.0
eps = 0.0001

err = 10.0
x_ant = x0
i = 0

while err>eps:
    x = x_ant-f(x_ant)/df(x_ant)    
    err = abs(x-x_ant)
    x_ant = x
    i=i+1
    print i, "| x=%.9f"%x, "| err=%.9f"%err