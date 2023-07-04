import matplotlib.pyplot as plt
import numpy as np
A=np.array([[[[[[[56, 168],[112, 224],[28, 392],[56/3, 280],[196, 140],[140, 504],[84, 33.6]]]]]]]).reshape(7,2)
print(A)
plt.scatter(A[:, 0], A[:, 1])
plt.show()
