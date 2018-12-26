"""
Author: Uchenna Edeh
Given an array of integers and a number k, where 1 <= k <= length of array, compute the maximum values of each subarray of length k.

for example, give array = [10, 5, 2, 7, 8, 7] and k = 3, we should get [10, 7, 8, 8], since:

	10 = max(10, 5, 2)
        7 = max(5, 2, 7)
        8 = max(2, 7, 8)
        8 = max(7, 8, 7)

solve in contant time and 0 space.
Algo:
iterate over array. have a second loop iterate over sub list if element left is at least ( n - i >= k ).
"""
import sys

def solution1(my_list, k):
    length_list = len(my_list)
    for i, _ in enumerate(my_list):
        if (i + k) <= length_list:
            max_num = 0
            for j in my_list[i:i+k]:
                if j > max_num:
                    max_num = j
            print(max_num)
            

def main(args):
    if len(args) != 3:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}' {2} \n\tExpected Result: {3}\n\tPlease Try Again!\n\t".format( __file__, '10,5,2,7,8,7', '3', '10,7,8,8' ))
    print(solution1([int(x) for x in args[1].split(',')], int(args[2])))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)

