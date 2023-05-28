import numpy as np
import pandas as pd
import scipy as sp

FACTORIZACION_CARTEL = """
 _____________________
|                     |  
| FACTORIZACION DE LU |
|_____________________|
                        """
RESOLUCION_CARTEL = """
 ________________________________
|                                |  
| RESOLUCION DE LA FACTORIZACION |
|________________________________|
                        """

# Función principal del algoritmo de lu
def lu(A, B):
    L, U = calculador_LU(A)
    dict_LU = {' MATRIZ L:': L,' MATRIZ U:': U}

    imprimir_matrices_formateadas(FACTORIZACION_CARTEL, dict_LU)

    y = calculador_vector(L,B)
    x = calculador_vector(U, y)

    print(RESOLUCION_CARTEL)
    print(f" VECTOR Y:\n  {np.round(y, decimals = 2)}\n\n VECTOR X:\n  {np.round(x, decimals = 2)}\n")
    
    return x

# Calcula y retorna las matrices L y U
def calculador_LU(A):
    _, L, U = sp.linalg.lu(A)
    return (L, U)

# Calcula el valor de la incognita en la ecuación matricial
def calculador_vector(matriz, resultado):
    return np.linalg.solve(matriz, resultado)

# Calcula el número máximo de operaciones elementales a realizar
# para despejar la matriz dada utilizando el método de
# sustitución hacia adelante
def calculador_op_max_adelante(matriz):
    n = matriz.shape[0]
    return (n**2) - n

# Calcula el número máximo de operaciones elementales a realizar
# para despejar la matriz dada utilizando el método de
# sustitución hacia atras
def calculador_op_max_atras(matriz):
    n = matriz.shape[0]
    return n**2

# Imprime un título y matrices con sus respectivos subtitulos
def imprimir_matrices_formateadas(titulo, dict_formateado):
    print(titulo)
    for (nombre, matriz) in dict_formateado.items():
        print(nombre)
        imprimir_matriz(matriz)

# Imprime matriz columna por columna
def imprimir_matriz(matrix):
    for row in matrix:
        print(f'  {np.round(row, decimals = 2)}')
    print()