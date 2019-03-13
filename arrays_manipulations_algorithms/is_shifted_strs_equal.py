"""
Author: Uchenna Edeh
Given two strings A and B, return whether or not A can be shifted some number of times to get B.
Example, if A is 'abdcde' and B is 'cdeab', return true. If A is 'abc' and B is 'acb', return False
"""

def solution(A, B):
    # Validation goes here
    #print((type))
    if not isinstance(A, str):
        raise ValueError("Ivalid input data used. Input data must str but {0} is used.".format(type(A).__name__))

    if not isinstance(B, str):
        raise ValueError("Ivalid input data used. Input data must str but {0} is used.".format(type(B).__name__))

    if not len(A) or not len(B):
        raise ValueError('Input data must be non-empty...')

    if len(A) != len(B):
        return False

    i = 0
    len_a = len(A)

    while(i < len_a):
        A = A[1:] + A[:1]
        if A == B:
            return True

        i = i + 1

    return False

print(solution('abcde', 'cdeab'))
print(solution('abc', 'acb'))
print(solution('abc', 'acb'))
print(solution('abcde', 'ecba'))
#print(solution('abcde', ''))
print(solution('abcde', ['U','C','H','E']))


