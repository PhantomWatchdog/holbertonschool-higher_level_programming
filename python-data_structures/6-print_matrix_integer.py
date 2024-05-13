#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        #for num in row:
        #print("{:d}".format(num), end=' ') #Display a space at end
        print(" ".join(["{:d}".format(num) for num in row]))
