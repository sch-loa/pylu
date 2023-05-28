import numpy as np

class ColumnSizeDifference(Exception):
    def __init__(self):
        super().__init__("El número de columnas de los elementos matriciales debe coincidir")

class NonSquareMatrix(Exception):
    def __init__(self):
        super().__init__("La matriz debe ser cuadrada")

class NonLUOperable(Exception):
    def __init__(self):
        super().__init__("La determinante de cada submatriz debe ser distinta de cero") 

# Verifica que dos matrices/vectores tengan el mismo
# número de columnas para poder hacer operaciones entre las mismas.
def is_column_size_different(A, B):
    if(A.shape[0] != B.shape[0]):
        raise ColumnSizeDifference

# Verifica que la matriz sea cuadrada
def is_square(A):
    if(A.shape[0] != A.shape[1]):
        raise NonSquareMatrix

def is_lu_operable(A):
    n = A.shape[0]
    for i in range(1, n+1):
        submatriz = A[:i, :i]
        det = np.linalg.det(submatriz)
        if det == 0:
            raise NonLUOperable