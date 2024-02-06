# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:44:05 2017

@author: israe
"""

import math
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

X = np.array([ 1., 2., 3., 4., 5., 6.])
Y = np.array([ 47., 65., 92., 132., 190., 275.])

Yl = np.log(Y) 
Xl = np.log(X)

# montando a matriz do sistema
A11 = np.sum(Xl * Xl)
A12 = np.sum(Xl)
A22 = len(Xl)
B1 = np.sum(Xl*Yl)
B2 = np.sum(Yl)

A = np.array([[A11,A12],[A12,A22]])
B = np.array([B1,B2])

a = solve(A, B)
print (a)

# lista de pontos para os plots
Xr = np.linspace(X[0], X[-1], 51)
#reta
h = lambda X: a[0]*X + a[1]
# plotando
plt.plot(X, Y, "r.", Xr, h(Xr), "-") 
plt.grid()
plt.show()
  
# hipérbole
k = math.exp(a[1])
b = a[0]
g = lambda Xl: k*np.power(Xl,b)

Yr = g(Xr)
print Yr

# plotando
plt.plot(X, Y, "r.", Xr, g(Xr), "-") 
plt.grid()
plt.show()

print g(7)
