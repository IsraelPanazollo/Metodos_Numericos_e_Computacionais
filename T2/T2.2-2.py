# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 16:58:50 2017

@author: israe
"""

import math

f = lambda x: math.log(x)-x+2
df = lambda x: (1/x) - 1 

x0 = 3.1

err = 10.0
x_ant = x0
i = 0

while err>0.0001:
    x = x_ant-f(x_ant)/df(x_ant)    
    err = abs(x-x_ant)
    x_ant = x
    i=i+1
    print i, "| x=%.9f"%x, "| err=%.9f"%err