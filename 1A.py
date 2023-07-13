import numpy as np
matrizA = np.array([[[4, 2, 3], [9, 5, 6], [7, 3, 4]]]).reshape(3,3)
print("matriz A", matrizA)
C = matrizA * 56
print("")
print(C)
print("")
matrizB = np.array([[[7, 8, 4], [9, 6, 9], [12, 5, 6]]]).reshape(3,3)
print("matriz B", matrizB)
D = matrizB * 56
print("")
print(D)
print("")
E=C+D
print("Ventas semanales", E)
print("ventas totales por fruta", np.sum(E, axis=0))
