# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 17:40:47 2016

@author: buriol
"""
import math

# Método da bisseção
#-------------------------------
f = lambda x: x**2 + math.log(x)
#-------------------------------
a = 0.1
b = 1.0
eps = 0.01
#-------------------------------

# Apenas inicializando
err = 10.0
amp = b-a
x_ant = a
i = 0

n_max = (math.log10(b-a) - math.log10(eps))/math.log10(2)
print ("Estimativa do número de iterações: ", n_max)

while err>eps and err>amp:
    xm = (a+b)/2.0
    if f(xm)*f(a)<0:
        b = xm
    else:
        a = xm
    print (i,"|xm=%.9f"%xm,"|f(a)=%.9f"%f(a),"|f(xm)=%.9f"%f(xm),"|f(b)=%.5f"%f(b),"|err=%.5f"%err,"|amp=%.5f"%amp)
    amp = (b-a)/2.0    
    err = abs((xm-x_ant)/xm)
    x_ant = xm
    i=i+1
    
    
