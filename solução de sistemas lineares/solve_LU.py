# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:54:30 2016

@author: buriol
"""
import numpy as np
import scipy
import scipy.linalg

import solve_L

A = [[3.,1.,1.], 
     [1.,3.,0.], 
     [0.,2.,2.]] 
b = [8.,6.,4.]

#print scipy.linalg.solve(A,b)
#A = [[2.,0.,1.], 
#     [0.,2.,1.], 
#     [1.,1.,3.]] 

#A = [[2.0, 3.0, 1.0, 5.0 ],
#     [1.0, 3.5, 1.0, 7.5 ],
#     [1.4, 2.7, 5.5, 12. ],
#     [-2., 1.0, 3.0, 28. ]] 
#b = [11., 13., 21.6, 30.]

#A = [[1.,1.,1.], 
#     [2.,1.,-1.], 
#     [3.,2.,0.]] 

#A = [[2.,1.,2.], 
#     [1.,2.,3.], 
#     [4.,1.,2.]] 
     
#A = [[2., 3., 1., 5.],
#     [1., 3.5, 1., 7.5],
#     [1.4, 2.7, 5.5, 12.],
#     [-2., 1., 3., 28.]]
#     
#b = [11., 13., 21.6, 30.]


#funcao fatorar uma matriz A em um produto LU
def factor_LU(A):
    n = len(A)     
    U=[]  # cria uma lista vazia
    L=[]  # cria uma lista vazia
    for i in range(n):
        U.append([0]*n) # preenche uma matriz nxn de zeros
        L.append([0]*n) # preenche uma matriz nxn de zeros
    
    for m in range(n):
        L[m][m] = 1
        
        soma = 0    
        for k in range(n):
            soma +=  L[m][k]*U[k][m]
        U[m][m] = A[m][m]-soma   
        
        for j in range(m,n):
            soma = 0
            for k in range(m):
                soma +=  L[m][k]*U[k][j]
            U[m][j]=A[m][j]-soma
        
        for i in range(m+1,n):
            soma = 0
            for k in range(m+1):
                soma +=  L[i][k]*U[k][m]
            L[i][m] = (A[i][m]-soma)/U[m][m]

    return L,U

L, U = factor_LU(A)
##L=scipy.array(L)
##U=scipy.array(U)
#print "L=", L
#print "U=", U
#
##print L.dot(U)
#def solve_L(L, b):
#    x1 = b[0]/L[0][0]
#    x = [x1]
#    for i in range(1,len(L)):
#        soma = 0
#        for j in range(0,i):
#            soma +=  L[i][j]*x[j]
#        x.append((b[i]-soma)/L[i][i])
#    return x

y = solve_L.solve(L, b)
print ("y=", y)

#U = [[2.0, 3.0, 1.0, 5.0], [0, 2.0, 0.5, 5.0], [0, 0, 4.65, 6.999999999999998], [0, 0, 0, 18.483870967741936]]
#y = [ 11.        ,   7.5       ,  11.65      ,  18.48387097]

#funcao para resolver um sistema triangula superior U
def solve_U(A, b):
    n = len(A)-1       #os indices correm de 0 ate n-1
    xn = b[n]/A[n][n]

    x = [0]*len(A)     # cria um vetor de zeros    
    x[-1] = xn         # atribui xn na ultima posicao de x
    
    for i in range(n-1,-1,-1):
        soma = 0
        for j in range(i+1,n+1):
            soma +=  A[i][j]*x[j]
        xi = (b[i]-soma)/A[i][i]
        x[i] = xi
    return x
    
x = solve_U(U, y)
print ("x=",x)
