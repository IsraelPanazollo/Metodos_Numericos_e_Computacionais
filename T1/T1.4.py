# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:30:43 2017

@author: israe
"""

print "O número pi é aproximadamente: "

x=0

for n in range(50):
    x = x + ((-1.)**n)/(1+ (2.*n)) 
     
pi = 4. * x

print pi

