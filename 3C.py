import numpy as np
import sympy as sp
from sympy import *
#defino los vectores como columnas de una matriz
m1=np.array([[[56, 112, 336],[392, 784, 2688],[-448, -896, -3136]]]).reshape(3,3)
print(m1)
#defino la matriz en sympy
m1_sympy= Matrix(m1)
#reducción de gauss
rref, pivots = m1_sympy.rref()
print(np.array(rref))
num_pivots = len(pivots)
free_vars = []
for i in range(m1.shape[1]):
   if i not in pivots:
    free_vars.append(i)
    print(free_vars)
