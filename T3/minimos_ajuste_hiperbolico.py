# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:29:25 2017

@author: buriol
"""

import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

X = np.array([ -3.0, -2.0, -1.0, -0.5, -0.4])
Y = np.array([ -0.13, -0.20, -0.49, -2.01, -4.99])
# plotando
plt.plot(X, Y, "o")
plt.grid()
plt.show()

Yl = np.power(Y, -1) 
print(Yl)
# plotando
plt.plot(X, Yl, "ro")
plt.grid()
plt.show()

# montando a matriz do sistema
A11 = np.sum(X * X)
A12 = np.sum(X)
A22 = len(X)
B1 = np.sum(X*Yl)
B2 = np.sum(Yl)

A = np.array([[A11,A12],[A12,A22]])
B = np.array([B1,B2])

a = solve(A, B)
print (a)

# lista de pontos para os plots
Xr = np.linspace(X[0], X[-1], 50)

#reta
h = lambda X: a[0]*X + a[1]
# plotando
plt.plot(X, Yl, "r.", Xr, h(Xr), "-") 
plt.grid()
plt.show()
  
# hipérbole
g = lambda X: np.power(a[0]*X+a[1], -1)
Yr = g(Xr)
# plotando
plt.plot(X, Y, "r.", Xr, g(Xr), "-") 
plt.grid()
plt.show()
#
#
#
#
#
