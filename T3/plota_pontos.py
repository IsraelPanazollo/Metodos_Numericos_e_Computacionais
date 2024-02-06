# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

X = [-0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
Y = [-0.25, -0.5, 0.25, 0.0, 0.75, 1.5, 1.25, 1.00, 1.75, 2.5, 2.25]

## Plota os pontos 
plt.grid()
plt.plot(X, Y,"x") 
plt.show()
