"""
Author: Uchenna Edeh
We can determin how out of order an array A is by counting the number of inversions it has. 
Two elements A[i] and A[j] form a inversion if A[i] > A[j] but i < j. That is, a smaller
element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

Example, a sorted list has zero inversions. The array [2,4,1,3,5] has three inversions: (2,1), (4,1), and (4,3).
The array [5,4,3,2,1] has ten inversions: every distinct pair forms an inversion.
"""
import sys

def solution1(A):
    count = 0
    for i, val in  enumerate(A):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                count = count + 1
    #        print(A[i], A[j])

    return count

def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, "2,4,1,3,5", '3' ))
    A = [int(x) for x in args[1].split(',')]
    print(solution1(A))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)

