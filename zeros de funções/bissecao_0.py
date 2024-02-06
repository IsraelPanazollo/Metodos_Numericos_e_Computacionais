#import math
from math import log as ln
a = 0.1
b = 1.0
err = 10
x_ant = 0.0

while err > 0.01:
    x = (a+b)/2
    prod = (x**2 + ln(x)) * (a**2 + ln(a))
    
    if prod < 0:
        b = x
    else:
        a = x

    err = abs(x - x_ant)/abs(x)
    x_ant = x

    print (x)




