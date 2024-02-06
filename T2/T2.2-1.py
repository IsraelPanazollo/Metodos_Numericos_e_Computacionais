# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 16:44:06 2017

@author: israe
"""

import math

phi = lambda x: math.log(x) + 2

x0 = 3.1

err = 10.0
x_ant = x0
i = 0

while err>0.0001:
    x = phi(x_ant)
    err = abs(x-x_ant)/abs(x)
    x_ant = x
    i=i+1
    print (i, "| x=%.9f"%x, "| err=%.9f"%err)
   