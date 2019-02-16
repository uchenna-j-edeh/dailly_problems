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
    max_lpw = ''
    for i, val in enumerate(A):
        start = i
        end = len(A)
        #for j in range(i+1, end):
         j = i + 1 
         start = i
         is_even = False
         is_odd = False
         while(j <= end - 1):
            if start < 0:
                break 
            if is_odd is False and A[j] == A[start]:
                lpw = A[start : j + 1]
                is_even = True
                is_odd = False
        
            if is_even is False and j + 1 <= end and A[j + 1] == A[start]:
                lwp = A[start : j + 1]
                is_odd = True
                is_odd = False

            if len(max_lpw) < len(lpw):
                max_lpw = lpw

            start = start - 1
            j = j + 1

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

