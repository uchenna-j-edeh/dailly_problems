"""
Given a sorted list of integers, square the elements and give the output in sorted order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
steps:
find the index of the lowest positive #.
from there interate left and right comparing the results of both side and placing them in sorted order
"""
import math

def solution(my_list):
    # find the lowest positive, we could use binary search too
    lowest_positive = 0
    
    for i, val in enumerate(my_list):
        if val > 0 and val < lowest_positive:
            lowest_positive = i
    if i == 0:
        return my_list

    new_list = []
    k = 0
    j = i - 1
    while k < len(my_list):
        if j < 0:
            for u in range(i, len(my_list)):
                new_list.append(math.square(u))
            return
        if i >= len(my_list):
            for v in len(my_list):
                if j - 1 < 0:
                    return
                new_list.append(math.square(j-1))

        nsquare = math.square(my_list[i])
        psquare = math.square(my_list[j])

        if psquare < nsquare:
            new_list.append(psquare)
            i += 1
        elif nsquare < psquare:
            new_list.append(nsquare)
            j -= 1
        else:
            new_list.append(psquare)
            new_list.append(nsquare)
            i += 1
            j -= 1
            k += 1

        k += 1


        


    
