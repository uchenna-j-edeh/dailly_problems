"""
Problem Statement
In this problem, you have to implement the findSum(lst,value) function which will take a number n as input and return two numbers that add up to n.

Input
A list and a number n

Output
A list with two integers a and b that add up to n

Sample Input
lst = [1,21,3,14,5,60,7,6]
n = 81
Sample Output
lst = [21,60]
"""
def findSum(lst, value):
    hash = dict()
    for i in lst:
        hash[i] = 1

    for j in lst:
        my_diff = value - j
        if hash.get(my_diff, False):
            return [j, my_diff]

print(findSum([1,21,3,14,5,60,7,6], 81)) 
