# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:28:49 2016

@author: buriol
"""

import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

X = np.array([-2., -1., 0, 1., 2., 3.])
Y = np.array([19.01, 3.99, -1.00, 4.01, 18.99, 45.00])

# Calcula os elementos das marizes
A11 = 0
A12 = 0
A13 = 0
A22 = 0
A13 = 0
A23 = 0

for x in X:
    A11 = A11 + x**4
    A12 = A12 + x**3
    A13 = A13 + x**2
    A23 = A23 + x

B1 = np.sum((X.dot(X)).dot(Y)) 
B2 = np.sum(X.dot(Y))
B3 = np.sum(np.array(Y))

# Monta e resolve o sistema
A = np.array([[A11,A12, A13],[A12, A12, A13], [A13, A23, len(X)]])
B = np.array([B1,B2,B3])
a = solve(A, B)
print (a)

# define a funcao g(x) para plotar 
g = lambda x: a[0]*x*x+a[1]*x+a[2]

# cria pontos (x, y) da reta 
Xr = np.arange(X[0], X[-1]+1, 1)
Yr = []
for x in Xr:
    Yr.append(g(x))    

# Plota os pontos e a reta
plt.plot(X, Y, "ro", Xr, Yr, "-") 
plt.show()




