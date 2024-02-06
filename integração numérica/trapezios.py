# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:08:23 2016

@author: buriol
"""

import numpy as np
h = 0.5

# Criando 7 pontos (6 subintervalos) igualmente espaçados no intervalo [1, 4]
X = np.linspace(1.0, 4.0, 7)

# Função a ser integrada
f = lambda x: np.sqrt(x)

# Regra dos trapézios usando funções do numpy
It = (h/2)*(f(X[0]) + 2*np.sum(f(X[1:6:1])) + f(X[-1]))

print "Resultado: ", It