# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 15:39:06 2017

@author: israe
"""


A = [[6.1, 0.32, 1.3, 2.1, 0.11], 
     [0.82, 8.81, 1.01, 3., 3.12], 
     [0.5, 1.78, 15.2, 4.2, 8.1],     
     [4.2, 5.3, 1.8, 20.9, 7.51],     
     [0.2, 9.1, 4.68, 4.3, 20.1]] 

b = [19.52, 15.83, -22.14, 27.28, -21.78]

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
