"""
Author: Uchenna Edeh
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""
import sys

def solution1(my_list):
    for i, val in enumerate(my_list):
        for k in range(i, len(my_list)):
            if my_list[k] == my_list[i]:
                break
            return my_list[i]


def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, '6,1,3,3,3,6,6', '1' ))
    print(solution1([int(i) for i in args[1].split(',')]))
    #print(solution2([int(x) for x in args[1].split(',')]))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)

