# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 13:49:09 2017

@author: israe
"""
# Importando a biblioteca padrao para funcoes matematicas
# import math
# Funcoes trigonometricas podem ser chamadas fazendo math.cos(x) ou math.sin(x)

import matplotlib.pyplot as plt

# Definindo a lista de pontos a serem interpolados
X  = [5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0]
Y  = [49.0, 105.0, 172.0, 253.0, 352.0, 473.0, 619.0, 793.0]    
dd = []    # Cria uma lista vazia para armazenar as diferencas divididas

# Inserindo na lista de diferencas divididas a lista de dif. div. de ordem 0 
dd.append(Y) 
# ...imprimindo para conferir     
#print (dd[0])

# Gerando a tabela de diferecas divididas a partir da ordem 1 em diante
for ordem in range(1, len(X), 1):
    dd.append([])   # Adiciona uma lista vazia para armazenar as dds de ordem 1
    
    # Para cada ordem, calcula a lista de valores resultantes
    for k in range(0, len(X)-ordem, 1): 
        #print (ordem, k)
        #print (dd[ordem-1][k+1],dd[ordem-1][k],x[k+ordem], x[k]) 
        valor = (dd[ordem-1][k+1]-dd[ordem-1][k])/(X[k+ordem]-X[k])    
        #print (valor)        
        dd[ordem].append(valor)
    #print (dd[ordem])

def produtorio(x,n):
    prod = 1.
    for i in range(n):
        prod = prod * (x-X[i])
    return prod


def calculaP(x):
    soma = dd[0][0]
    for i in range(1,len(X)):
        soma = soma + produtorio(x,i)*dd[i][0]
    return soma

print ("P(",12.,")", calculaP(12.)) 
print ("P(",32.,")", calculaP(32.)) 
print ("P(",31.,")", calculaP(31.)) 
 
plt.plot(X, Y, "ro") # Plota os pontos dados 
plt.plot(X, Y, "-") # Plota o polinomio com linha
plt.grid() # Cria uma grid
plt.show() # Mostra  
    
