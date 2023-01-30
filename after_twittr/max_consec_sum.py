"""
    Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

def max_sum_array(arr):
    # iterate through array
    # set the max array to be the first int
    # then start comparing from first
    # if you find something bigger update varaibale, store index, otherwise start at new index
    # max_sum = arr[0]
    # val = arr[0]
    max_so_far  = arr[0]
    max_ending_here = 0
    for a in arr:
        max_ending_here = max_ending_here + a
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


print(max_sum_array([34, -50, 42, 14, -5, 86]))

print(max_sum_array([-34, -1, -42, -14, -5, -86]))





