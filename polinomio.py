#interpolacion polinomial
import numpy as np
import matplotlib.pyplot as plt
A=np.array([[625,125,25,5,1],[6561,729,81,9,1],[2401,343,49,7,1],[4096,512,64,8,1],[50625,3375,225,15,1]])
invA=np.linalg.inv(A)

b=np.array([[8],[2],[4],[12],[18]])
X=(invA @ b)

print("Matriz A:",A)
print("Matriz b:",b)
print("Matrix X:",X)

m=np.linspace(0,20,num=10000)
polynomial=[2.11550000e+03, -1.09291369e+03, 2.02913690e+02, -1.59434524e+01, 4.43452381e-01]
poly_coefs = polynomial[::-1]
y=np.polyval(poly_coefs, X)
plt.show()
#plt.axes()
#plt.plot(m,y)
