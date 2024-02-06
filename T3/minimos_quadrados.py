# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:57:40 2016

@author: buriol
"""

import matplotlib.pyplot as plt

X = [183., 173., 168., 188., 158., 163., 193., 163., 178.]
Y = [79., 69., 70., 81., 61., 63., 79., 71., 73.]

g1 = lambda x: x**2
g2 = lambda x: 1

A = [[]]
soma = 0.0

for x in X:
    soma = 
    A[0].append()

#def calculaP(x):
#    valor = 0
#    for k in range(len(Y)):
#        lk = 1.0
#        for i in range(len(X)):
#            if k != i:
#                lk = lk*(x - X[i])/(X[k]-X[i])
#        print "l",k,"(",x,")"," = ", lk
#        valor = valor +Y[k]*lk 
#    return valor
#
#x = 0.23
#
#p = calculaP(x)
#
#Xplot = []
#Yplot = []
#for i in range(100):
#    xplot = X[0] + i*((X[-1]-X[0])/100)
#    Xplot.append(xplot)
#    yplot = calculaP(xplot)
#    Yplot.append(yplot)
#print Xplot

#plt.plot(Xplot, Yplot) 

plt.plot(X, Y, "ro") 
plt.show()

print "P(",x,") =", p