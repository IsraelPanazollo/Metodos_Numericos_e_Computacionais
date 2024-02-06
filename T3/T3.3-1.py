# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 14:30:45 2017

@author: israe
"""
from scipy.linalg import solve
import matplotlib.pyplot as plt
import numpy as np

# Dados do exercicio
X = np.array([50.0, 52.0, 54.0, 56.0 , 58.0, 60.0])
Y = np.array ([2.75, 1.45, 0.5, 0.15, 0.2, 0.85])

# Calcula os elementos das marizes
a11 = np.sum(X**4)
a12 = np.sum(X**3)
a13 = np.sum(X**2)
a23 = np.sum(X)
a33 = len(X)
b1 = np.sum(Y * X**2)
b2 = np.sum(X * Y)
b3 = np.sum(Y) 

# Monta e resolve o sistema
A = np.array([[a11, a12, a13],
              [a12, a13, a23], 
              [a13, a23, a33]])

B = np.array([b1, b2, b3])

a = solve(A, B)
print (a)

# define a funcao g(x) para plotar 
g = lambda x: a[0]*x**2 +a[1]*x + a[2]

Xv= - a[1]/(a[0]*2)
print Xv

Yv=g(Xv)
print Yv

# cria pontos (x, y) da reta 
Xr = np.linspace(X[0], X[-1], 50)

# Plota os pontos e a reta
plt.plot(X, Y, "ro", Xr, g(Xr), "-",Xv, Yv,"x" )
plt.grid() 
plt.show()


Xr = np.linspace(56.5, 56.6, 50)

# plotando
plt.plot(Xr, g(Xr), "-", Xv, Yv,"ro") 
plt.grid()
plt.show()
