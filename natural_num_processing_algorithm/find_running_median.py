# -*- coding: utf-8 -*-
"""
Author: Uchenna Edeh
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
1
3.0
5
6
7
Note median of odd list is the middle one
[2]                     = > 2
[2, 1]                  => 3/2 = 1.5
[2, 1, 5]               => 1
[2, 1, 5, 7]            => 6/2 =3
[2, 1, 5, 7, 2]         => 5
[2, 1, 5, 7, 2, 0]      => 12/2 = 6
[2, 1, 5, 7, 2, 0, 5]   => 7

"""
import sys

def solution1(int_list):
    print(int_list)
    running_sum = 0
    first_middle = 0
    second_middle = 0
    for i, num in enumerate(int_list):
        #if i == 0:
        #    print(num)
        if (i + 1)% 2 == 0:
            indx = (i + 1) // 2
            first_middle = int_list[indx-1]
            second_middle = int_list[indx]
            median = (first_middle + second_middle) / 2
            print(median)
        else:
            indx = ((i + 1) // 2)
            result = int_list[indx]
            print(int(result))


def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, "2, 1, 5, 7, 2, 0, 5", '\n2,1.5,1,3,5,6,7'.replace(',', '\n')))
    solution1([int(x) for x in args[1].split(',')])

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)


