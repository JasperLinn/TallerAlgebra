import numpy as np
A=np.array([[[616, 560, 392],[1008, 616, 840],[1064, 448, 560]]]).reshape(3,3)
print("Ventas semanales", A)
print("")
A1=A[0]
A1M=A1[0]*2000
A1N=A1[1]*300
A1P=A1[2]*400
A1T=A1M+A1N+A1P
print("Ventas semanales Satélite", A1)
print("ventas semanales satélite de manzanas", A1M)
print("ventas semanales satélite de naranjas", A1N)
print("ventas semanales satélite de plátanos", A1P)
print("")
print("Ingreso total Satélite", A1T)

print("")
A2=A[1]
A2M=A2[0]*2000
A2N=A2[1]*300
A2P=A2[2]*400
A2T=A2M+A2N+A2P
print("Ventas semanales Central de manzanas", A2M)
print("Ventas semanales Central de manzanas", A2N)
print("Ventas semanales Central de manzanas", A2P)
print("")
print("Ingreso total Central", A2T)

print("")
A3=A[2]
A3M=A3[0]*2000
A3N=A3[1]*300
A3P=A3[2]*400
A3T=A3M+A3N+A3P
print("Ventas semanales San Francisco de manzanas", A3M)
print("Ventas semanales San Francisco de naranjas", A3N)
print("Ventas semanales San Francisco de plátanos", A3P)
print("")
print("Ingreso total San Francisco", A3T)

print("")
T=A1T+A2T+A3T
print("total ingresos semanal", T)
