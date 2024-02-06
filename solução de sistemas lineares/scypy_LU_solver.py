# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:28:55 2016

@author: buriol
"""
import scipy
import scipy.linalg

A = scipy.array([[2., 3., 1., 5.],
     [1., 3.5, 1., 7.5],
     [1.4, 2.7, 5.5, 12.],
     [-2., 1., 3., 28.]])
     
A1 = A[0:1,0:1]
A2 = A[0:2,0:2]
A3 = A[0:3,0:3]

print scipy.linalg.det(A1), scipy.linalg.det(A2), scipy.linalg.det(A3)
     
b = [11., 13., 21.6, 30.]

P, L, U = scipy.linalg.lu(A)
print P
print L
print U

print scipy.linalg.solve(A,b)

