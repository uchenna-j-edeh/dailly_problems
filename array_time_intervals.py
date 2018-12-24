"""
Author: Uchenna Edeh
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
Algorithm
iterate over tuples with each tuple first
count overlap as 0 and count non overlap as 2
"""
import sys
def solution1(my_list):
    #print (list_tuples)
    for i, _list in enumerate(my_list):
        x, y = int(_list[0]), int(_list[1])
        for k in my_list[i+1:]: 



def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, "30,75;0,50;60,150", '2' ))
    my_list = [x.split(',') for x in args[1].split(';')]
    solution1(my_list)

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)

