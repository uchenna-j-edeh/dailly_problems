"""
Problem Statement
Implement a function reArrange(lst) which sorts the elements such that all the negative elements appear on the left and positive elements appear at the right.

Output
A list with negative elements at the left and positive elements at the right

Sample Input
[10,-1,20,4,5,-9,-6]
Sample Output
[-1,-9,-6,10,20,4,5]
"""

def reArrange(lst):
    i = 0

    while(i < len(lst)):
        if abs(lst[i]) == lst[i]:
            temp = lst[i]
            del lst[i]
            lst.append(temp)
        i = i + 1

    return lst

print(reArrange([10,-1,20,4,5,-9,-6]))
