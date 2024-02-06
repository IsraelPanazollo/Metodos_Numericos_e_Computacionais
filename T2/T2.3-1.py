#-*- coding: utf-8 -*-
import math
erro = 10.0
x0 = 0.0
x1 = 0.01
i=0
w0=1/(math.sqrt(0.3*40*10**(-6)))
a=1/(2*200*40*10**(-6))
wd=math.sqrt(w0**2-(a**2))

def f(t):
	return (50*math.exp(-1*a*t)*math.cos(wd*t))-10

#parte 1
while erro> 0.0001:
	t1 = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
	erro = abs(t1-x1)/abs(t1)
	x0 = x1
	x1 = t1
	i+=1
	print (i,"| t1 = %.9f"%t1)
print "_________________________________________________________"

#parte 2
x2=0.015
x3=0.020
j=0
erro2=1.

while erro2> 0.0001:
	t2 = (x2*f(x3)-x3*f(x2))/(f(x3)-f(x2))
	erro2 = abs(t2-x3)/abs(t2)
	x2 = x3
	x3 = t2
	j+=1
	print (j,"| t2=%.9f"%t2)
print "_________________________________________________________"

#parte 3
x4=0.021
x5=0.03
k=0
erro3=1.

while erro3> 0.0001:
	t3 = (x4*f(x5)-x5*f(x4))/(f(x5)-f(x4))
	erro3 = abs(t3-x5)/abs(t3)
	x4 = x5
	x5 = t3
	k+=1
	print (k,"| t3=%.9f"%t3)


