"""
Author: Uchenna J. Edeh
Given an array of integers, return a new array such that each element at index i of the new array is the product
of all the numbers in the the original array except the original one at i.
"""
import sys
import math

def solution1(args):
    all_products = 1 
    new_list = []
    for i in args:
        all_products = all_products * i

    for i, _ in enumerate(args):
        new_list.append(int(all_products / args[i]))

    return new_list

def solution2(args):
    "solve without using division. Use logarithim or n^-1. We would use n^-1"
    all_products = 1
    new_list = []

    for i in args:
        all_products = all_products * i

    for _, val in enumerate(args):
        result = math.pow(val, -1)
        new_list.append(int(result * all_products))

    return new_list
    
def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\t{0} {1} '{2}'\n\tExpected Result: {3}\n\tPlease Try Again!\n\t".format('python3', __file__, '1,2,3,4,5', '120,60,40,30,24' ))
    #print(solution1([int(x) for x in args[1].split(',')]))
    print(solution2([int(x) for x in args[1].split(',')]))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(0)
