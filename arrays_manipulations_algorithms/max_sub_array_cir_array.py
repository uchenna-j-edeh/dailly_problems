"""
Given a circular array, compute its maximum subarray sum O(n) time.
A subarray can be empty, and in this case the sum is 0
"""

import unittest

def max_sub_array(arr):
    sub_arr_sum = 0
    for a in arr:
        if a > 0:
            sub_arr_sum += a
    return sub_arr_sum


assert max_sub_array([8, -1, 3, 4]) == 15
assert max_sub_array([-4, 5, 1, 0]) == 6

print("Everything is OK!")


