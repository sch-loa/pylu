import numpy as np
from algorithms import lu
from exceptions import is_square, is_column_size_different, is_zero_or_natural

A_matrix = np.array([[3,-1,-1],[-1,3,1],[2,1,4]])
B_vector = np.array([1,3,7])

is_square(A_matrix) # Verifico que la matriz sea cuadrada
# Verifico que los vectores sean de tamaños equivalentes
is_column_size_different(A_matrix, B_vector)