"""
Author: Uchenna Edeh
Challenge: Given an array of integers, find the first missing positive in linear time and constant space. 
In other words, find the lowest positve int that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3,4,-1,1] should give 2. The input [1,2,0] should give 3.

Algorithm: transverse the array, keep track of the highest and lowest positive int. Ignore anything less or equal to 1. At the end, return lowest - 1 if it is defined or highest
"""
import sys
BIG_NUM = 1000000
def solution1(my_list):
    highest_int = 0
    lowest_int = BIG_NUM 

    import pdb; pdb.set_trace()
    for _, val in enumerate(my_list):
        if val <= 1:
            continue # just skip it

        if val > highest_int:
            highest_int = val

        if val < lowest_int:
            lowest_int = val

    if lowest_int == BIG_NUM:
        return highest_int + 1 

    return lowest_int - 1
        
def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, '3,4,-1,1', '2' ))
    X = [int(x) for x in args[1].split(',')]
    print(solution1(X))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(0)
