import numpy as np

def vectoreslinealmenteindependientes(v1, v2):
    # Convierte los vectores en NumPy arrays
    v1 = np.array(v1)
    v2 = np.array(v2)

    # Crea una matriz con los vectores como columnas
    matrix = np.column_stack((v1, v2))

    # Calcula el rango de la matriz
    rank = np.linalg.matrix_rank(matrix)

    # Revisa si el rango de la matriz es igual al número de vectores (Para este punto son 3 vectores)
    if rank == 2:
        return 'Los vectores son Linealmente Independientes'
    else:
        return 'los vectores son Linealmente Dependientes'

# Vectores del problema (N=1)
vector1 = [56, -3*56, 4*56]
vector2 = [56/5, 56*3/7, 3*56/13]

result = vectoreslinealmenteindependientes(vector1, vector2)

print(result)
