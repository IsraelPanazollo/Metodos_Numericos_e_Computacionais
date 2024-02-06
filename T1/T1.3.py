# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:56:36 2017

@author: israe
"""

from math import factorial as factorial

from math import e as e

print "Estimativa de número de Euler"

x = 0.
i = 0.
Erel = 1.

while(Erel > 0.0001):
    x = x + 1./factorial(i)
    i = i+1
    Erel = (e-x)/e

print x



 