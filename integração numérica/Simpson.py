# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:08:23 2016

@author: buriol
"""

import numpy as np
h = 0.25

# Criando 7 pontos (6 subintervalos) igualmente espaçados no intervalo [1, 4]
X = np.linspace(0.0, 3.0, 13)
print X

# Função a ser integrada
f = lambda x: x**2*np.exp(x)

# Regra dos trapézios usando funções do numpy
It = (h/2)*(f(X[0]) + 2*np.sum(f(X[1:12:1])) + f(X[-1]))
print "Resultado Trapézio: ", It

# Regra 1/3 de Simpson usando funções do numpy
Is = (h/3)*(f(X[0]) + 4*np.sum(f(X[1:12:2])) + 2*np.sum(f(X[2:12:2]))+ f(X[-1]))
print "Resultado 1/3 Simpson: ", Is

# Regra 3/8 de Simpson usando funções do numpy
Iss = (3*h/8)*(f(X[0]) + 3*np.sum(f(X[1:12:3])+f(X[2:12:3])) + 2*np.sum(f(X[3:12:3]))+ f(X[-1]))

print "Resultado 3/8 Simpson: ", Iss