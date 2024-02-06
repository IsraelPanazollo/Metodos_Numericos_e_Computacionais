# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 14:05:30 2017

@author: israe
"""

import matplotlib.pyplot as plt

# Dados do exercicio
X  = [5., 10., 15., 20., 25., 30., 35., 40.]
Y  = [49., 105., 172., 253., 352., 473., 619., 793.]    
# Funcao que calcula o valor do polinomio para um dado x
def calculaP(x):
    valor = 0
    for k in range(len(Y)):
        lk = 1.0
        for i in range(len(X)):
            if k != i:
                lk = lk*(x - X[i])/(X[k]-X[i])
        valor = valor +Y[k]*lk 

    return valor
print ("P(",12.,")", calculaP(12.)) 
print ("P(",32.,")", calculaP(32.)) 
print ("P(",31.,")", calculaP(31.)) 


# Cria a lista de pontos e calcula os valores para p plot
Xplot = []
Yplot = []
n = 20              # Numero de divisoes do intervalo de plot
dx = (X[-1]-X[0])/n # Incremento em x

# Preenche as listas X e Y para o plot 
for i in range(n+1):
    x = X[0] + i*dx
    y = calculaP(x)
    Xplot.append(x)
    Yplot.append(y)

# Plota
plt.plot(X, Y, "ro") # Plota os pontos dados 
plt.plot(Xplot, Yplot, "-") # Plota o polinomio com linha
#plt.grid(True) # Cria uma grid
plt.show() # Mostra