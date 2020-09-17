"""
implement quick sort algo
"""
import random

def quick_sort_helper(A, start, end):
    if start >= end:
        return

    # pick a random index for pivotal element
  #  indx = (end - start) // 2 
   # rand_index = indx + start 
   # print(A, indx)
    rand_index = random.randint(start, end)
    print(A, rand_index)

    A[rand_index], A[start] = A[start], A[rand_index]

    pivot = A[start]
    smaller = start
    bigger = start
    #import pdb; pdb.set_trace()

    for bigger in range(start + 1, end+1):
        if A[bigger] < pivot: # I found the orange value, less than pivot. So increment smaller
            smaller = smaller + 1
            A[smaller], A[bigger] = A[bigger], A[smaller]

    A[start], A[smaller] = A[smaller], A[start]
    quick_sort_helper(A, start, smaller - 1)
    quick_sort_helper(A, smaller + 1, bigger)


def quick_sort(A):
    quick_sort_helper(A, 0, len(A) - 1)


A = [9,1,5,6,3,4,9,0]
quick_sort(A)
print(A)
