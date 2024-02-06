# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:54:30 2016

@author: buriol
"""

A = [[2,0,0],
     [1,4,0],
     [1,1,1]] 

b = [2,-3,0]


#funcao para resolver um sistema triangula inferior
def solve(A, b):
    x1 = b[0]/A[0][0]
    x = [x1]
    for i in range(1,len(A)):
        soma = 0
        for j in range(0,i):
            soma +=  A[i][j]*x[j]
        x.append((b[i]-soma)/A[i][i])
    return x

print (solve(A,b))

    