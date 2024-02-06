# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:08:23 2016

@author: buriol
"""
import numpy as np
# Dados do enunciado
x0 = 0.0
xn = 3.0
n = 6
h = (xn-x0)/n
f = lambda x: x*np.exp(x)+1

# Criando n+1 pontos igualmente espacados 
X = np.linspace(x0, xn, n+1)
print (X)
print (np.round(f(X),4))

# Regra 1/3 de Simpson usando funções do numpy
I = (h/3)*(f(X[0]) + 4*np.sum(f(X[1:n:2])) + 2*np.sum(f(X[2:n:2]))+ f(X[-1]))
print ("Resultado 1/3 de Simpson: ", I)

