"""
Author: Uchenna J. Edeh
Given a matrix, print the diagonals...
"""

def solution1(matrix):
    left_diagonals = []
    right_diagonals = []
    for i, val0 in enumerate(matrix):
        for j, _ in enumerate(val0):
            if i == j:
                tab = '-'*(i+1)
                print(tab + repr(matrix[i][j]))
            indx = -1 * (i + 1)
            len_val = len(val0)
            if j == (len_val + indx): 
                tab = '-'*(len_val - i)
#                print(tab +  repr(matrix[i][indx]))




arrs = [
    ['x', 'o', 'x'],
    ['o', 'x', 'o'],
    ['x', 'o', 'x']
]

arrs2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#solution1(arrs2)
solution1(arrs)
