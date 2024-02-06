# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 22:06:34 2017

@author: israe
"""

A = [[-4.064, 2.008, 0., 0.], 
     [1.968, -4.128, 2.032, 0.], 
     [0., 1.928, -4.192, 2.072],     
     [0., 0., 1.872, -4.256]] 

b = [0., 0., 0., -10.64]

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

def solve_L(L, b):
    x1 = b[0]/L[0][0]
    x = [x1]
    for i in range(1,len(L)):
        soma = 0
        for j in range(0,i):
            soma +=  L[i][j]*x[j]
        x.append((b[i]-soma)/L[i][i])
    return x
        
y = solve_L(L, b)
print ("y=", y)

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
