import numpy as np
import pandas as pd
import scipy as sp

FACTORIZACION_CARTEL = """\033[F
 _____________________
|                     |  
| FACTORIZACION DE LU |
|_____________________|
                        """
RESOLUCION_CARTEL = """\033[F
 ________________________________
|                                |  
| RESOLUCION DE LA FACTORIZACION |
|________________________________|
                        """

# Función principal del algoritmo de lu
def lu(A, B):
    L, U, B_permutado = calculador_LU(A, B)
    dict_LU = {' MATRIZ L:': L,' MATRIZ U:': U}

    imprimir_matrices_formateadas(FACTORIZACION_CARTEL, dict_LU)

    y = calculador_vector(L, B_permutado)
    x = calculador_vector(U, y)

    print(RESOLUCION_CARTEL)
    print(f" VECTOR Y:\n  {np.round(y, decimals = 2)}\n\n VECTOR X:\n  {np.round(x, decimals = 2)}\n")
    
    return x

# Calcula y retorna las matrices L y U
# Devuelve el nuevo vector B con distinto orden
# en caso de que haya habido permutación
def calculador_LU(A, B):
    piv, L, U = sp.linalg.lu(A)
    B_permutado = piv @ B
    return (L, U, B_permutado)

# Calcula el valor de la incognita en la ecuación matricial
def calculador_vector(matriz, vector):
    return np.linalg.solve(matriz, vector)

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

def leer_matriz(filas, columnas):
    matriz = list()
    for i in range(1, filas + 1):
        fila = list()
        for j in range(1, columnas + 1):
            fila.append(float(input(f'|_ fila {i}, columna {j}: ')))
        if(i != filas):
            print('|')
        matriz.append(fila)
    return np.array(matriz)
            
def leer_vector(columnas):
    vector = list()
    for i in range(1, columnas + 1):
        vector.append(float(input(f'|_ columna {i}: ')))
    return np.array(vector)