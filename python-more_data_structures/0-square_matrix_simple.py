#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ''' result_matrix = []

    # Iterate over each row in the matrix
    for row in matrix:
        # Create a new row to store the squared values for the current row
        squared_row = []
        # Iterate over each element in the row and compute its square
        for num in row:
            squared_row.append(num ** 2)
        # Append the squared row to the result matrix
        result_matrix.append(squared_row)

    return result_matrix'''

    return [[num ** 2 for num in row] for row in matrix]
