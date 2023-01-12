#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        fields = []
        for j in range(len(matrix[i])):
            fields.append(matrix[i][j] ** 2)
        new_matrix.append(fields)
    return(new_matrix)
