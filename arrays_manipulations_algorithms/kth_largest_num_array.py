"""
Author: Uchenna Edeh
Given an array, find the kth largest int
Example: array => [11,10,9, 6, 8, 7, 0, 1, 4, 3,2, 5] where k = 3. Answer: 9
"""

def solution1(my_list, k):
    my_list = sorted(my_list)
    
    return my_list[len(my_list) - k]

my_list = [11,10,9, 6, 8, 7, 0, 1, 4, 3,2, 5]
k = 3
print(solution1(my_list, k))


