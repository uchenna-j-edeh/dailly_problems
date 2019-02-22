"""
Author: Uchenna Edeh
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
Algorithms:
use three variables
1. running_max_sum
2. max_sum
3. max_sum_from_last_smallest_num
"""
import sys

def solution1(A):
    max_sum_contiguos = A[0]
    current_sum = 0
    previous = 0

    for i, val in enumerate(A): 
        current_sum = val + current_sum   

        if current_sum  > max_sum_contiguos:        
            max_sum_contiguos = current_sum
        else:
           if val > current_sum:
               current_sum = val
           if current_sum > max_sum_contiguos:
               max_sum_contiguos = current_sum

    previous = val

    return max_sum_contiguos 
     

def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, "34, -50, 42, 14, -5, 86", '137' ))
    my_list = [int(x) for x in args[1].split(',')]
    print(solution1(my_list))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)

