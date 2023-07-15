import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
A=np.array([[[[[[[56, 168],[112, 224],[28, 392],[56/3, 280],[196, 140],[140, 504],[84, 33.6]]]]]]])
B=np.array([[[[[[56**6, 56**5, 56**4, 56**3, 56**2, 56, 1],[112**6, 112**5, 112**4, 112**3, 112**2, 112, 1],[28**6, 28**5, 28**4, 28**3, 28**2, 28, 1],[30840979456/729, 550731776/243, 9834496/81, 175616/27, 3136/9, 56/3, 1],[196**6, 196**5, 196**4, 196**3, 196**2, 196, 1],[140**6, 140**5, 140**4, 140**3, 140**2, 140, 1],[84**6, 84**5, 84**4, 84**3, 84**2, 84, 1]]]]]]).reshape(7,7)
print("matriz del sistema de ecuaciones", B)
C=np.array([[[[[[168],[224],[392],[280],[140],[504],[33.6]]]]]]).reshape(7,1)
print("")
print(C)
print("")
E=np.linalg.solve(B, C)
#print("solución sistema de ecuaciones", E)
R=np.linalg.inv(B) @ C
print("coeficientes del polinomio", R)








