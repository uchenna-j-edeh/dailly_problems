"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

How do we perform this four-way edge swap? One option is to copy the top edge to an array, and then move the left to the top, the bottom to the left, and so on. This requires O(N) memory, which is actually unnecessary.
A better way to do this is to implement the swap index by index. In this case, we do the following:
1 fori=0ton
2 temp= top[i];
3 top[i] = left[i]
4 left[i] = bottom[i] 5 bottom[i]= right[i] 6 right[i]= temp
"""
from pprint import pprint as pp

def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    n = len(matrix)
    for layer in range(0, n // 2):
        first = layer
        last = n - 1 - layer
        for i in range( first, last):
            offset = i - first
            top = matrix[first][i] # save top
            
            #left to top
            matrix[first][i] = matrix[last-offset][first]

            # bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]

            #right -> bottom
            matrix[last][last-offset] = matrix[i][last]

            #top -> right
            matrix[i][last] = top # right <- saved top

    return matrix


n_by_n_matrix = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11,],
        [13, 14, 15, 16]
        ]
result = [
        [13, 8, 4, 0],
        [14, 9, 5, 1],
        [15, 10, 6, 2],
        [16, 11, 7, 3],
        ]
print("The solution is :", rotate_matrix(n_by_n_matrix) == result)
