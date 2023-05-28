import numpy as np
from algorithms import lu, imprimir_matriz, calculador_op_max_adelante, calculador_op_max_atras
from exceptions import is_square, is_column_size_different

METODO_CARTEL = """
 ________________________________________________________________
|                                                                |
|                          METODO DE LU                          |
|________________________________________________________________|
|                                                                |
|  INTEGRANTES:                                                  |
|  |_ Loana Abril Schleich Garcia.                               |
|                                                                |
|  SISTEMA DE ECUACIONES A EVALUAR:                              |
|  |_ Ax = B, siendo:      ____________        ___        ____   |
|                     A = |  3  -1  -1 |  B = | 1 |  x = | x0 |  |
|                         | -1   3   1 |      | 3 |      | x1 |  |
|                         |  2   1   4 |      | 7 |      | x2 |  |
|                         |____________|      |___|      |____|  |
|________________________________________________________________|
|                                                                |
|                  FUNCIONAMIENTO DEL ALGORITMO                  |
|________________________________________________________________|
|                                                                |
|  Para aproximar el valor del vector x se descompone            |
|  la matriz A en dos partes:                                    |
|                                                                |
|  L -> Triangular inferior, con unos en su diagonal principal   |                                                 |
|  U -> Triangular superior                                      |
|                                                                |
|  Se descompone la ecuación en dos partes, tal que:             |
|    __                                                          |
|  _| Ly = B     Se resuelve la primera ecuación con el método   |
|   | Ux = y     de sustitución hacia adelante, y se reemplazan  |
|   |__          los valores en la siguiente con sustitución     |
|                hacia atrás.                                    |
|________________________________________________________________|

                """

NUMERO_OPERACIONES_CARTEL = """
 ________________________________________________________________
|                                                                |
|                NUMERO DE OPERACIONES ELEMENTALES               |
|________________________________________________________________|
|                                                                |
|  Es posible calcular el número de operaciones elementales en   |
|  el peor caso para una matriz genérica. Pero además, los       |
|  conocimientos que se tienen de ambas ecuaciones en nuestro    |
|  sistema reducen este número.                                  |
|                                                                |
|  -> Por cada elemento nulo se reduce una vez la cantidad de    |
|     sumas/restas y multiplicaciones necesarias.                |
|  -> Por cada elemento igual a uno se reduce una vez la         |
|     cantidad de multiplicaciones necesarias.                   |
|________________________________________________________________|
|                                                                |
|                   SUSTITUCION HACIA ADELANTE                   |
|________________________________________________________________|
|                                                                |
|  De la matriz L, se sabe que los elementos de la diagonal      |
|  principal son iguales a 1, y que todos los elementos          |
|  encima de la misma son nulos.                                 |
|  Para determinar el peor de los casos, asumimos que todos los  |
|  elementos restantes en la matriz son no nulos y distintos     |
|  de uno.                                                       |
|  Esto es, en términos matemáticos y para una matriz de nxn:    |
|                       Op_max = Op0 + Op1                       |
|  Donde Op_max es la cantidad total de operaciones a realizar,  |
|  siendo Op0 el número de sumas/restas y Op1 el número de       |
|  multiplicaciones                                              |
|                                                                |
|  -> Op0 = n^2 - n - j                                          |
|       Siendo j el número de elementos nulos. Como estos se     |
|       encuentran solo por encima de la diagonal, el número de  |
|       elementos nulos es equivalente a (n^2 - n)/2             |
|       Si igualamos el término a j y simplificamos, nos queda:  |
|                        Op0 = (n^2 - n)/2                       |
|  -> Op1 = n^2 - k                                              |
|       Siendo k el número de elementos nulos o iguales a 1.     |
|       Conociendo del cálculo anterior el valor de los          |
|       elementos nulos, y sabiiendo que el número de elementos  |
|       iguales a 1 equivale a n, si igualamos la suma de ambos  |
|       términos a k y simplificamos, la fórmula final es:       |
|                        Op1 = (n^2 - n)/2                       |
|  Nótese que Op0 y Op1 son exactamente iguales. Esto es debido  |
|  a que la matriz es cuadrada. Finalmente, se simplifica a:     |
|                        Op_max = n^2 - n                        |
|________________________________________________________________|
|                                                                |
|                     SUSTITUCION HACIA ATRAS                    |
|________________________________________________________________|
|                                                                |
|  De a matriz U, se sabe que todos los elementos debajo de la   |
|  diagonal principal son nulos. Asumimos que el resto de los    |
|  elementos son no nulos y distintos de uno. Es decir, se       |
|  toman en cuenta todos los elementos menos los que se          |
|  encuentran por encima de la diagonal principal.               |
|                       Op_max = Op0 + Op1                       |
|  -> Op0 = n^2 - n - j                                          |
|  -> Op1 = n^2 - j                                              |
|  Tomando j de los cálculos anteriores y simplificando la       |
|  expresión, se obtiene finalmente:                             |
|                          Op_max = n^2                          |
|________________________________________________________________|

                            """

A_matrix = np.array([[3,-1,-1],[-1,3,1],[2,1,4]])
B_vector = np.array([1,3,7])

is_square(A_matrix) # Verifico que la matriz sea cuadrada
# Verifico que los vectores sean de tamaños equivalentes
is_column_size_different(A_matrix, B_vector)

print(METODO_CARTEL)
print(' MATRIZ A:')
imprimir_matriz(A_matrix)

print(' VECTOR B:')
print('  ' + str(B_vector))
print()

x = lu(A_matrix, B_vector)

print(f" Solución final: {np.round(x, decimals = 2)}")
print(f" Evaluación de la solución en A: {np.round(np.sum(A_matrix * x, axis = 1), decimals = 2)}\n")

print(NUMERO_OPERACIONES_CARTEL)

total_y_ops = calculador_op_max_adelante(A_matrix)
total_x_ops = calculador_op_max_atras(A_matrix)
print(f" Número máximo de operaciones para despejar el vector y: {total_y_ops}")
print(f" Número máximo de operaciones para despejar el vector x: {total_x_ops}")
print(f" Total de operaciones en el peor caso: {total_y_ops + total_x_ops}\n")