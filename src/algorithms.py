import numpy as np
import pandas as pd
import re
import scipy as sp

def lu(A, B):
    L, U = calculador_LU(A)

# Calcula y retorna las matrices L y U
def calculador_LU(A):
    _, L, U = sp.linalg.lu(A)
    return (L, U)

# Imprime un título y matrices con sus respectivos subtitulos
def imprimir_matrices_formateadas(titulo, dict_formateado):
    print(titulo)
    for (nombre, matriz) in dict_formateado.items():
        print(nombre)
        imprimir_matriz(matriz)

# Imprime matriz columna por columna
def imprimir_matriz(matrix):
    for row in matrix:
        print('  ' + str(np.round(row, decimals = 2)))
    print()

# Actualiza los valores del DataFrame con los resultados de la ecuación matricial
# y su evaluación en la matriz inicial.
def actualizar_dataframe(df, i, x, Ax):
    dic = pd.DataFrame({
        'Iteración': i,
        'Aproximación de x': str(np.round(x, decimals = 6)),
        'Evaluación de x en A': str(np.round(Ax, decimals = 6))
    } , index = range(1))
   
    return pd.concat([df, dic], axis = 0, ignore_index = True)

#Convierte la una colección de números en una lista
# usando expresiones regulares
def a_lista(array_strings):
    occurs = list()
    for fila in array_strings: 
        occur = re.findall(r"\d+(?:\.\d+)?", fila)
        occur = np.array([float(oc) for oc in occur])
        occurs.append(occur)
    return occurs