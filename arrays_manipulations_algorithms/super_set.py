"""
Author: Uchenna Edeh
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
You may also use a list or array to represent a set.
"""

import sys

def solution1(my_set):
    print(my_set)

    power_set = []

    for k, _ in range(2, my_set):
        for i in range(k, len(my_set):
            for j in range(i, len(my_set)):


def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, "1,2,3", '\n{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}'))
    print(solution1(args[1].split(',')))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)

