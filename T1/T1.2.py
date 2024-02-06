# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 21:54:48 2017

@author: israel
"""
from math import e as e
from numpy import arange as arange
from decimal import Decimal 
def a(x):
    return (e**(1./x))/(e**(1./x)+1)

def b(x):
    return 1./(e**(-1./x)+1)
    
for i in arange(0.001, 0.1, 0.01 ):
    print "Para x = "  + str(i)
    print "a = ", Decimal(a(i))
    print "b = ", Decimal(b(i))
    
    

