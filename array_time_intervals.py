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
    counter = 0 
    seenit = []
    for i, _list in enumerate(my_list):
    #    x, y = int(_list[0]), int(_list[1])
#        import pdb; pdb.set_trace()
        for k in range(i+1, len(my_list)): 
            if is_overlapped(_list, my_list[k]):
                if my_list[k] not in seenit:
                    counter = counter + 2 # any overlap reduces the max possible time slots by 1

                seenit.append(my_list[k])

    return counter

def is_overlapped(first_array, second_array):
    x, y = int(first_array[0]), int(first_array[1])
    m, n = int(second_array[0]), int(second_array[1])

    if x >= m and x <= n or m >= x and m <= y:
        return True

    return False

def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, "30,75;0,50;60,150", '2' ))
    my_list = [x.split(',') for x in args[1].split(';')]
    print(solution1(my_list))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)

