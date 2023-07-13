import numpy as np

matrizA = np.array([[[4, 2, 3], [9, 5, 6], [7, 3, 4]]]).reshape(3,3)
print("matriz A", matrizA)
print("")
C = matrizA * 56
print("total 1", C)
print("")

matrizB = np.array([[[7, 8, 4], [9, 6, 9], [12, 5, 6]]]).reshape(3,3)
print("matriz B", matrizB)
print("")
D = matrizB * 56
print("total 2", D)
print("")
E=C+D
print("Ventas semanales", E)


print("Número total de ventas por puesto", np.sum(E, axis=1))
print("")
print("Puesto con mayor número de ventas: plaza central", np.max(np.sum(E, axis=1)))
