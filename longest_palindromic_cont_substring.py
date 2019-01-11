"""
Author: Uchenna Edeh
Given a string, find the longest palindromic contiguous substring. 
If there are more than one with the maximmum length, return any one.

For example, the longest palindromic substring of 'aabcdch' is 'bcdcb'. 
The longest palindromic substring of 'bananas' is 'anana'
"""
import sys

def solution1(A):
    lpw = ''
    for i, val in enumerate(A):
        start = i
        end = len(A)
        #for j in range(i+1, end):
         j = 0
         while(j <= end - 1):
            if start < 0:
                break 
            if A[i+1] == A[start]:
                lpw = A[start : j + 1]
            if i+2 < end and A[i+2 ] == A[start]:
                lwp = A[start : j + 2]
                
            else:
                break
            start = start - 1

    return lpw


def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, "aabcdcb", 'bcdcb' ))
    print(solution1(args[1]))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)

