
class ColumnSizeDifference(Exception):
    def __init__(self):
        super().__init__("El número de columnas de los elementos matriciales debe coincidir")

class NonSquareMatrix(Exception):
    def __init__(self):
        super().__init__("La matriz debe ser cuadrada")

class NegativeNumber(Exception):
    def __init__(self):
        super().__init__(f"El campo numérico debe ser positivo")

# Verifica que dos matrices/vectores tengan el mismo
# número de columnas para poder hacer operaciones entre las mismas.
def is_column_size_different(A, B):
    if(A.shape[0] != B.shape[0]):
        raise ColumnSizeDifference

# Verifica que la matriz sea cuadrada
def is_square(A):
    if(A.shape[0] != A.shape[1]):
        raise NonSquareMatrix

# Verifica que un número sea cero o natural
def is_zero_or_natural(value):
    if(value < 0):
        raise NegativeNumber()