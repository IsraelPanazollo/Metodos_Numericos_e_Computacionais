# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 18:12:43 2017

@author: israe
"""

import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

X = np.array([73., 69., 70., 81., 61., 63., 79., 71., 73.])
Y = np.array([183., 173., 168., 188., 158., 163., 193., 163., 178.])

# Calcula os elementos das marizes
a11 = np.sum(X*X)
a12 = np.sum(X)
a22 = len(X)
b1 = np.sum(X * Y)
b2 = np.sum(Y)

# Monta e resolve o sistema
A = np.array([[a11, a12],
              [a12, a22]])

B = np.array([b1,b2])

a = solve(A, B)
print (a)

# define a funcao g(x) para plotar 
g = lambda x: a[0]*x+a[1]

# cria pontos (x, y) da reta 
Yr = []
for x in X:
    Yr.append(g(x)) 
  

# Plota os pontos e a reta
plt.plot(X, Y, "ro", X, Yr, "-")
plt.grid() 
plt.show()

