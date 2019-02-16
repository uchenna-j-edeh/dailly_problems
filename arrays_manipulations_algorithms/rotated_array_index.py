"""
Author: Uchenna Edeh
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
Algorithm: Check elements at both sides. Transverse through the side that has element with value closer to the our given element.
Another idea is to use binary search to find point at which the high and low exist. Then apply another BS in the second half.
"""

def solution1(my_list, elem):
    first_index = my_list[0]
    last_index = my_list[-1]

    first_diff = abs(first_index - elem)
    last_diff = abs(last_index - elem)
    
    if last_diff < first_diff:
        print('going in through the left')
        len_list = len(my_list)
        idx = len_list - 1
        for i, val in enumerate(my_list):
            if my_list[idx -i] == elem:
                return idx - i
            
            #if my_list[idx - i] < element or my_list[idx - i] > element:
            #    return 
    else:
        print('going in through the right')
        for i, val in enumerate(my_list):
            if val == elem:
                return i
            #if val > element or 

def solution2(arr, 


_list = "13, 18, 25, 2, 8, 10"
element = 18
#element = 8
#element = 9
print(solution1([int(i) for i in _list.split(',')], element)) 
