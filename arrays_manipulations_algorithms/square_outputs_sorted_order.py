"""
Given a sorted list of integers, square the elements and give the output in sorted order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
steps:
find the index of the lowest positive #.
from there interate left and right comparing the results of both side and placing them in sorted order
"""
import math

def square(x):
    return x * x

def solution(my_list):
    # find the lowest positive, we could use binary search too
    biggest_positive = float('inf') 
    idx = 0 
    for i, val in enumerate(my_list):
        if val >= 0 and val < biggest_positive:
            biggest_positive = val
            idx = i
            print(idx)

    if idx == 0:
        return my_list

    new_list = []
    k = 0
    i = idx
    j = idx - 1
    nsquare = square(my_list[j])
    psquare = square(my_list[i])
    while k < len(my_list):

        print('j ==> ', j)
        print('i ==> ', i)


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

        if i+1 >= len(my_list):
            #i = 1
            psquare = float('inf')
        else:
            nsquare = square(my_list[j])

        if j - 1 < 0:
            #j += 1
            nsquare = -1 * float('inf')
        else:
            psquare = square(my_list[i])

        k += 1

    return new_list

print(solution( [-9, -2, 0, 2, 3]))
