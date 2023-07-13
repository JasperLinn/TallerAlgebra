import numpy as np
matrizA=np.array([[[4,2,3],[9,5,6],[7,3,4]]]).reshape(3,3)
print("matriz A", matrizA)
C= matrizA * 56
print("ventas 1",C)
E=np.transpose(C)
print("ventas plátanos", E[2])
print(np.max(E[2]))


matrizB=np.array([[[7,8,4],[9,6,9],[12,5,6]]]).reshape(3,3)
print("matriz B", matrizB)
D= matrizB * 56
print("ventas 2",D)
F=np.transpose(D)
print("ventas plátanos", F[2])
print("plaza central", np.max(F[2]))
