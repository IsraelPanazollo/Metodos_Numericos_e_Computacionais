# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:08:23 2016

@author: buriol
"""

import numpy as np
h = 4.0/60
n=10
X = np.array([0,4,8,12,16,20,24,28,32,36,40])
Y = np.array([24,23,31,36,40,45,48,52,55,60,62])
# Criando 7 pontos (6 subintervalos) igualmente espaçados no intervalo [1, 4]
#X = np.linspace(0.0, 40.0, n)

# Função a ser integrada
#f = lambda x: np.sqrt(x)

print (Y[1:n:1])


# Regra dos trapézios usando funções do numpy
It = (h/2)*(Y[0] + 2*np.sum(Y[1:n:1]) + Y[-1])
print ("Resultado: ", It)

# Regra 1/3 de Simpson usando funções do numpy
I = (h/3)*(Y[0] + 4*np.sum(Y[1:n:2]) + 2*np.sum(Y[2:n:2])+ Y[-1])
print ("Resultado 1/3 de Simpson: ", I)