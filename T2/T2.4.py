# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:55:27 2016

@author: buriol
"""
import math

# Método de Newton-Raphson
#-------------------------------
def f(x):
	return 16.628*(1.702*(x-300) + (0.0045405*(x**2 - 300**2)) - 0.00072133333*(x**3-300**3) - 20000)

def df(x):
	return 16.628*(-0.00216 * x**2 + 0.009081 * x + 1.702)

#-------------------------------
x0 = -130.0
eps = 0.00001
#-------------------------------

# Apenas inicializandoas variáveis
err = 10.0
x_ant = x0
i = 0

while err>eps:
    x = x_ant-f(x_ant)/df(x_ant)    
    err = abs(x-x_ant)
    x_ant = x
    i=i+1
    print i, "| x=%.9f"%x, "| err=%.9f"%err
