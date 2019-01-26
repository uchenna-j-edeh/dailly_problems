"""
Author: Uchenna Edeh
Challenge: Given an array of integers, find the first missing positive in linear time and constant space. 
In other words, find the lowest positve int that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3,4,-1,1] should give 2. The input [1,2,0] should give 3.
Algo: If we can use efficient sorting alog to sort in place for linear time, then another linear time to pass through the list, we can solve in linear time
"""
import sys
BIG_NUM = 1000000
def solution1(my_list):
    lowest_int = my_list[0] 
    prev_num = lowest_int
    print(my_list)
    #import pdb; pdb.set_trace()
    # store in dict
    for i, val in enumerate(my_list):
        if i == 0:
            continue

        if 1 + prev_num == 0:
            prev_num = val
            continue

        if 1 + prev_num != val:
            return 1 + prev_num 

        prev_num = val

    return my_list[-1] + 1
        
def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, '3,4,-1,1', '2' ))
    X = [int(x) for x in args[1].split(',')]
    print(solution1(sorted(X)))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(0)
