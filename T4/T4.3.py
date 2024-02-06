# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 22:15:32 2017

@author: israe
"""

X = [0., 2., 4., 6., 8., 10., 12.]
Px = [4., 3.95, 3.8, 3.6, 3.41, 3.3, 3.2]
Ac= [100., 103., 110., 120., 133., 150., 171.]

n= len(X)-1
i=0
L=12.
h = L/n

Y = []
for k in range(len(X)):
    Y.append(Ac[i]*Px[i])
    i=i+1

#print Y

# Regra 1/3 de Simpson usando funções do numpy
I = (h/3)*(Y[0] + 4*(Y[1]+Y[3]+Y[5]) + 2*(Y[2]+Y[4])+ Y[6])
print ("Resultado 1/3 de Simpson: ", I)

