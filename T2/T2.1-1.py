# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 19:02:02 2017

@author: israe
"""

import math

f =lambda x: 1.24 - 0.5*math.pi + math.asin(x)+ x*math.sqrt(1-x**2) 

i = 0
a = 0.0
b = 0.2
err = 10
x_ant = 0.0

while err > 0.0001:
    x = (a+b)/2
    prod = f(x) * f(a)
    
    if prod < 0:
        b = x
    else:
        a = x

    err = abs(x - x_ant)/abs(x)
    x_ant = x
    i = i+1
    print i, "| x=%.9f"%x, "| err=%.9f"%err