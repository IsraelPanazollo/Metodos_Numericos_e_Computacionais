# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:08:23 2016

@author: buriol
"""

import numpy as np
# Dados do enunciado
x0 = 1.0
xn = 4.0
n = 6
h = (xn-x0)/n
f = lambda x: np.sqrt(x)

# Criando n+1 pontos igualmente espacados 
X = np.linspace(x0, xn, n+1)


# Regra dos trapézios usando funções do numpy
It = (h/2)*(f(X[0]) + 2*np.sum(f(X[1:n:1])) + f(X[-1]))
print "Resultado Trapézio: ", It
