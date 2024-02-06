# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:06:52 2016

@author: buriol
"""
import numpy as np
# Dados do enunciado
x0 = 1.0
xn = 7.0
n = 9
h = (xn-x0)/n
f = lambda x: np.log(x+9)

# Criando n+1 pontos igualmente espacados 
X = np.linspace(x0, xn, n+1)

# Regra 3/8 de Simpson usando funções do numpy
I = (3*h/8)*(f(X[0]) + 3*np.sum(f(X[1:n:3])+f(X[2:n:3])) + 2*np.sum(f(X[3:n:3]))+ f(X[-1]))

print "Resultado: ", I