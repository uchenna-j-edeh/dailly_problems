"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

Note: |x| is the absolute value of x
    """

def diagonalDifference(arr):
    # Write your code here
    lr_diag_sum = 0
    rl_diag_sum = 0
    count = 0
    j_dx = len(arr) - 1
    for i in range(len(arr)):
        # i_dx = i + count
        for j in range(len(arr[i])):
            if count == i and j_dx - count == j:
                rl_diag_sum += arr[i][j]
            if i == j: # lr diagonal
                lr_diag_sum += arr[i][j]
        count += 1

    diff = lr_diag_sum - rl_diag_sum
    if diff < 0:
        diff = -1 * diff
    return diff

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]


print(diagonalDifference(arr))

arr2 = [
[11, 2, 4],
[4, 5, 6],
[10, 8, -12]
]

print(diagonalDifference(arr2))