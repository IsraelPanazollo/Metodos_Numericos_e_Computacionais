# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 23:40:30 2017

@author: israe
"""

import math
erro = 10.0
w0=1/(math.sqrt(0.3*40*10**(-6)))
al=1/(2*200*40*10**(-6))
wd=math.sqrt(w0**2-(al**2))

def f(t):
	return (50*math.exp(-1*al*t)*math.cos(wd*t))-10

#parte 1
i = 0
a = 0.0
b = 0.01
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
    
#parte 2
i = 0
a = 0.015
b = 0.02
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
    
#parte 3
i = 0
a = 0.021
b = 0.025
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