import numpy as np
A=np.array([[1,2,2,1],[3,4,8,1]])
B=np.array([[4,5,6,7],[9,8,7,21]])
C = A+B
D= A*B
E=np.transpose(A)
F= E @ B

print("Matriz A", A)
print("Matriz B", B)
print("Matriz C:", C)
print("A^t", E)
print("A^tB", F)

X=np.array([[2,5,7],[2,7,9],[4,9,-9]])
detX=np.linalg.det(X)
print("Determinante X:",detX)
invX=np.linalg.inv(X)
b=np.array([[5],[-27],[4]])
X1=invX @ b
X2=np.linalg.solve(X,b)
print("variables x2",X2)
print("Matrix X:",X)
print("Variables X1:",X1)
print(np.allclose(np.dot(X,X1),b))