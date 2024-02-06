# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:55:27 2016

@author: buriol
"""
from math import cos

# Método das aproximações sucessivas (ou ponto fixo)
#-------------------------------
phi = lambda x: cos(x)
#-------------------------------
x0 = 0.7
eps = 0.01
#-------------------------------

# Apenas inicializandoas variáveis
err = 10.0
x_ant = x0
i = 0

while err>eps:
    x = phi(x_ant)
    err = abs(x-x_ant)/abs(x)
    x_ant = x
    i=i+1
    print (i, "| x=%.9f"%x, "| err=%.9f"%err)
   