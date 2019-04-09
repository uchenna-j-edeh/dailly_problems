"""
Problem Statement
Implement a function findSecondMaximum(lst) which returns the second largest element in the list.

Input:
A List

Output:
Second largest element in the list

Sample Input
[9,2,3,6]
Sample Output
6
"""

def findSecondMaximum(lst):
    max_val = lst[0]

    for val in lst:
        if val > max_val:
            max_val = val

    second_max_val = -1 * float("inf")

    for val in lst:
        if val > second_max_val and val != max_val:
            second_max_val = val


    return second_max_val


print(findSecondMaximum([9,2,3,6]))

