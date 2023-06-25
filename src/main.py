import numpy as np
from algorithms import lu, imprimir_matriz, calculador_op_max_adelante, calculador_op_max_atras, leer_matriz, leer_vector
from exceptions import is_square, is_column_size_different, is_lu_operable

METODO_CARTEL = """
 ____________________________________________________________________________
|                                                                            |
|                                METODO DE LU                                |
|____________________________________________________________________________|
|                                                                            |
|  INTEGRANTES:                                                              |
|  |_ Loana Abril Schleich Garcia.                                           |
|                                                                            |
|  SISTEMA DE ECUACIONES A EVALUAR:                                          |
|  |_ Ax = B, siendo:                                                        |
|____________________________________________________________________________|
|                                                                            |
|                        FUNCIONAMIENTO DEL ALGORITMO                        |
|____________________________________________________________________________|
|                                                                            |
|  Para aproximar el valor de x se transforma la matriz A en el producto de  |
|  dos matrices:                                                             |
|                                                                            |
|  L -> Triangular inferior, con unos en su diagonal principal               |
|  U -> Triangular superior                                                  |
|                                                                            |
|  Se descompone el sistema en dos partes, tal que:                          |
|    __                                                                      |
|  _| Ly = B     Se resuelve la primera ecuación con el método de            |
|   | Ux = y     sustitución hacia adelante, y se reemplazan los valores en  |
|   |__          la siguiente, resolviéndola con sustitución hacia atrás.    |
|____________________________________________________________________________|
                """

NUMERO_OPERACIONES_CARTEL = """\033[F
 ____________________________________________________________________________
|                                                                            |
|                      NUMERO DE OPERACIONES ELEMENTALES                     |
|____________________________________________________________________________|
|                                                                            |
|  Es posible calcular el número de operaciones elementales en el peor caso  |
|  para una matriz genérica de nxn. Esto es, en términos matemáticos:        |
|                             Op_max = Op0 + Op1                             |
|  Donde Op_max es la cantidad total de operaciones a realizar, siendo Op0   |
|  el número de sumas/restas y Op1 el número de multiplicaciones. Por        |
|  combinatoria se sabe que el número de sumas/restas en una matriz es       |
|  equivalente al número de elementos en la misma menos el numero de         |
|  columnas. Esto es porque estamos contando la cantidad de espacios entre   |
|  elementos, que es donde se realiza la operación. Y para las               |
|  multiplicaciones, como estamos contando la cantidad de productos entre    |
|  los pares elemento matricial-elemento vectorial, el valor es igual a      |
|  la cantidad de elementos de la matriz. Nos queda:                         |
|                   Op0 = n^2 - n                Op1 = n^2                   |
|  Pero además, los conocimientos que se tienen de ambas ecuaciones en       |
|  nuestro sistema reducen ese número.                                       |
|                                                                            |
|  -> Por cada elemento nulo se reduce una vez la cantidad de sumas/restas   |
|     y multiplicaciones necesarias.                                         |
|  -> Por cada elemento igual a uno se reduce una vez la cantidad de         |
|     multiplicaciones necesarias.                                           |
|                                                                            | 
|  Para los elementos desconocidos se asume el peor caso, es decir, que son  |
|  no nulos y distintos de uno.                                              |
|____________________________________________________________________________|
                            """

SUSTITUCION_ADELANTE_CARTEL = """\033[F
 ____________________________________________________________________________
|                                                                            |
|                         SUSTITUCION HACIA ADELANTE                         |
|____________________________________________________________________________|
|                                                                            |
|  De la matriz L, se sabe que los elementos de la diagonal principal son    |
|  iguales a 1, y todos los elementos encima de esta son nulos. Entonces:    |
|                                                                            |
|  -> Op0 = n^2 - n - j                                                      |
|     Siendo j el número de elementos nulos. Como estos se encuentran solo   |
|     por encima de la diagonal, el número de elementos nulos es igual a     |
|     (n^2 - n)/2 Si igualamos el término a j y simplificamos, nos queda:    |
|                              Op0 = (n^2 - n)/2                             |
|  -> Op1 = n^2 - k                                                          |
|       Siendo k el número de elementos nulos o iguales a 1. Conociendo del  |
|       cálculo anterior el valor de los elementos nulos, y sabiendo que el  |
|       número de elementos iguales a 1 equivale a n, si igualamos la suma   |
|       de ambos términos a k y simplificamos, la fórmula final es:          |
|                              Op1 = (n^2 - n)/2                             |
|                                                                            |
|  Nótese que Op0 y Op1 son exactamente iguales. Esto es debido a que la     |
|  matriz es cuadrada. Finalmente, se simplifica a:                          |
|                              Op_max = n^2 - n                              |
|____________________________________________________________________________|
                            """

SUSTITUCION_ATRAS_CARTEL = """\033[F
 ____________________________________________________________________________
|                                                                            |
|                           SUSTITUCION HACIA ATRAS                          |
|____________________________________________________________________________|
|                                                                            |
|  De la matriz U, se sabe que todos los elementos debajo de la diagonal     |
|  principal son nulos.                                                      |
|                                                                            |
|  -> Op0 = n^2 - n - j                                                      |
|  -> Op1 = n^2 - j                                                          |
|                                                                            |
|  Tomando j de los cálculos anteriores y simplificando la expresión, se     |
|  obtiene finalmente:                                                       |
|                                Op_max = n^2                                |
|____________________________________________________________________________|
                            """

#A_matrix = np.array([[3,-4,5,-7],[1,2,-4,5],[2,-4,5,-1],[3,-1,7,5]])
#B_vector = np.array([19,31,21,10])

n = int(input('Cantidad de filas/columnas de la matriz: '))
print('\nMATRIZ A:')
A_matrix = leer_matriz(n,n)
print('\nVECTOR B:')
B_vector = leer_vector(n)

is_square(A_matrix) # Verifico que la matriz sea cuadrada
# Verifico que los vectores sean de tamaños equivalentes
is_column_size_different(A_matrix, B_vector)
is_lu_operable(A_matrix) # Verifico que la determinante de cada submatriz dentro de A sea != 0
print('\nLa determinante de cada submatriz de A es nula, es posible operar con el método de LU')

print(METODO_CARTEL)
print(' MATRIZ A:')
imprimir_matriz(A_matrix)

print(' VECTOR B:')
print(f'  {str(B_vector)}\n')

# RESOLUCIÓN DEL SISTEMA
x = lu(A_matrix, B_vector)
print(f" Solución final: {np.round(x, decimals = 2)}")
print(f" Evaluación de la solución en A: {np.round(np.sum(A_matrix * x, axis = 1), decimals = 2)}\n")

# TOTAL DE OPERACIONES ELEMENTALES EN EL PEOR CASO
print(NUMERO_OPERACIONES_CARTEL)
total_y_ops = calculador_op_max_adelante(A_matrix)
total_x_ops = calculador_op_max_atras(A_matrix)
print(f"{SUSTITUCION_ADELANTE_CARTEL}\n Número máximo de operaciones para despejar el vector y: {total_y_ops}\n")
print(f"{SUSTITUCION_ATRAS_CARTEL}\n Número máximo de operaciones para despejar el vector x: {total_x_ops}\n")
print(f"\n TOTAL DE OPERACIONES ELEMENTALES EN EL PEOR CASO: {total_y_ops + total_x_ops}\n")