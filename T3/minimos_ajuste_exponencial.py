# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:52:12 2017

@author: buriol
"""
import math
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

X = np.array([ -1.0, -0.9, -0.8, 0.0, 1.0, 2.0])
Y = np.array([ 6.01, 5.39, 4.80, 2.01, 0.65, 0.21])
# plotando
plt.plot(X, Y, "ro")
plt.grid()
plt.show()

Yl = np.log(Y) 
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
Xr = np.linspace(X[0], X[-1], 51)
#reta
h = lambda X: a[0]*X + a[1]
# plotando
plt.plot(X, Yl, "r.", Xr, h(Xr), "-") 
plt.grid()
plt.show()
  
# hipérbole
k = math.exp(a[1])
b = math.exp(a[0])
g = lambda X: k*np.power(b,X)

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
