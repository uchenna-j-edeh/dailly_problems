"""
Given a sorted list of integers, square the elements and give the output in sorted order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
steps:
find the index of the lowest positive #.
from there interate left and right comparing the results of both side and placing them in sorted order
"""
def solution(my_list):
    # find the lowest positive, we could use binary search too
    lowest_positive = 0
    
    for i, val in enumerate(my_list):
        if val > 0 and val < lowest_positive:
            lowest_positive = i

    new_list = []
    for i in range(len(my_list)):
        if 


    
