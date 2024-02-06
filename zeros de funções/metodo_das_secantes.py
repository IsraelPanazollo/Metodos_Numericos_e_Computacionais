#-*- coding: utf-8 -*-

err = 1.0
x0 = 0.0
x1 = 1.0

f = lambda x: x**3 - 0.5

while err> 0.01:
    x = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
    err = abs(x-x1)/abs(x)   # calcula o erro relativo
   
    x0 = x1
    x1 = x
    
    print ("| x=%.4f"%x)

