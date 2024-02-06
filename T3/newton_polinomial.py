# -*- coding: utf-8 -*-
"""
Created on Fri May  6 01:04:37 2016
@author: buriol
"""
# Importando a biblioteca padrao para funcoes matematicas
# import math
# Funcoes trigonometricas podem ser chamadas fazendo math.cos(x) ou math.sin(x)

import matplotlib.pyplot as plt
import numpy as np

# Definindo a lista de pontos a serem interpolados
X  = [0., 0.5, 1.0]
Y  = []    # Cria uma lista vazia para armazenar os valores de yi
dd = []    # Cria uma lista vazia para armazenar as diferencas divididas

# Definindo a função a ser interpolada
#f = lambda x: math.cos(math.sin(x*math.pi))
f = lambda X:np.exp(X)+np.sin(X)

# Atribuindo os valores de f(xi) na lista de valores yi
for i in range(len(X)):
    Y.append(f(X[i]))
# ...imprimindo para conferir 
print ("Y=", Y)

# Inserindo na lista de diferencas divididas a lista de dif. div. de ordem 0 
dd.append(Y) 
# ...imprimindo para conferir     
print (dd[0])

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
    print (dd[ordem])



def calculaP(x):
    valor = dd[0][0]
    for i in range(1, len(X)-1, 1):
        print (valor)
        prod = 1.0
        for n in range(i+1):
            prod = prod * (x-X[n])  
            valor = valor + prod*dd[n+1][0]
    return valor

print (calculaP(0.7))
 


    

    
    
