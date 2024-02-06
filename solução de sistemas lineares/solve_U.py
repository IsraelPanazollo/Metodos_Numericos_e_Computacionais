# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:54:30 2016

@author: buriol
"""

#funcao para resolver um sistema triangular superior
def solve(U, y):
    n = len(U)-1       #os indices correm de 0 ate n-1
    xn = y[n]/U[n][n]

    x = [0]*len(U)     # cria um vetor de zeros    
    x[-1] = xn         # atribui xn na ultima posicao de x
    
    for i in range(n-1,-1,-1):
        soma = 0
        for j in range(i+1,n+1):
            soma +=  U[i][j]*x[j]
        xi = (y[i]-soma)/U[i][i]
        x[i] = xi
    return x

#U = [[ 4.,  0., -3.],
#     [ 0., -4.,  3.25 ],
#     [ 0.,  0.,  4.375]]
       
#y=[-2., 10.5, 8.75]

#print solve_U(U,y)
       
       
