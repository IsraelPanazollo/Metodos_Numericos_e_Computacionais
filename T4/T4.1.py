# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 14:00:41 2017

@author: israe
"""
import numpy as np

n=12
x0=0.
xn=3.
h = (xn-x0)/n

# Função a ser integrada
f = lambda x: (x**2.) * np.exp(x)

# Criando n+1 pontos igualmente espacados 
X = np.linspace(x0, xn, n+1)

# Regra dos trapézios usando funções do numpy
I1 = (h/2)*(f(X[0]) + 2*np.sum(f(X[1:n:1])) + f(X[-1]))
print ("Resultado Regra dos Trapezios: ", I1)

# Regra 1/3 de Simpson usando funções do numpy
I2 = (h/3)*(f(X[0]) + 4*np.sum(f(X[1:n:2])) + 2*np.sum(f(X[2:n:2]))+ f(X[-1]))
print ("Resultado 1/3 de Simpson: ", I2)

# Regra 3/8 de Simpson usando funções do numpy
I3 = (3*h/8)*(f(X[0]) + 3*np.sum(f(X[1:n:3])+f(X[2:n:3])) + 2*np.sum(f(X[3:n:3]))+ f(X[-1]))
print ("Resultado 3/8 de Simpson: ", I3)