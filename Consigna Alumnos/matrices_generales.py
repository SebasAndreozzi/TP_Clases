from random import randint
import listas_generales

###IMPRIME MATRIZ
def print_matrix(matrix:list):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end = " ")
        print("")

###GENERA MATRIZ DE ALEATORIOS
def random_matrix(line:int, column:int, minimum:int, maximum:int) -> list:
    result = [[0] * column for _ in range(line)]

    for i in range(line):
     for j in range(column):
         result[i][j] = randint(100,999)

    return result

###SUMA TODOS LOS ELEMENTOS DE UNA MATRIZ
def matrix_element_addition(matrix:list) -> int|float:
    result = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result += matrix[i][j]
    
    return result

###SUMA COLUMNAS
def matrix_column_addition(matrix:list) -> list:
    result = [0] * len(matrix[0])

    position_counter_column = -1

    for i in range(len(matrix[0])):
        position_counter_column += 1

        result[position_counter_column] = listas_generales.column_addition(matrix, i)

    return result
    
###SUMA FILAS
def matrix_line_addition(matrix:list) -> list:
    result = [0] * len(matrix)

    position_counter_line = -1


    for i in range(len(matrix)):
        position_counter_line += 1

        result[position_counter_line] = listas_generales.line_addition(matrix,i)
    
    return result

###SUMA DIAGONAL DERECHA-IZQUIERDA
def right_diagonal_addition(matrix:list) -> int|float:

    result = 0

    for i in range(len(matrix)):
        result += (matrix[i][i])
         
    return result

###SUMA DIAGONAL IZQUIERDA-DERECHA
def left_diagonal_addition(matrix:list) -> int|float:

    result = 0

    position_counter = -1

    for i in range(len(matrix)-1, -1, -1):
        
        position_counter += 1
        result += (matrix[i][position_counter])