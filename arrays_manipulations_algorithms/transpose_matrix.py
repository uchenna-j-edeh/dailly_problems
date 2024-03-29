"""
Leetcode
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
"""

def transpose(matrix):
    transpose = []
    for i in range(len(matrix[0])): # i = 0, 
        for j in range(len(matrix)): # j = 0, 1
            if len(transpose) < j+1: # True
                transpose.append([]) # [ [] ]

            transpose[j].append(matrix[i][j])     # [[1]]

    return transpose   


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(transpose(matrix))
