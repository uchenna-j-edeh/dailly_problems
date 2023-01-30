"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0
"""

def zero_col_row(matrix):
    for i in len(matrix):
        for j in len(matrix[i]):
            if matrix[i][j] == 0:
                for k in len(matrix[i]):
                    matrix[i][k] = 'x'

                for m in len(matrix):
                    matrix[j][n] = 'x'

    for u in len(matrix):
        for v in len(matrix[u]):
            if matrix[u][v] == 'x':
                matrix[u][v] = 0


                



    

        