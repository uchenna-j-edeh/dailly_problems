"""Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""

def subarray(input):
    max_product = 0
    if len(input) > 1 :
        max_product = input[0] * input[1]
    else:
        raise("You need a list at least 2")

    i = 0
    for mp in max_product:
        



