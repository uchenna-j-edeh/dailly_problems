"""
Implement disision of two positive integers without using the division, multiplication or modulous operator.
Return the quotient as an integer, ignoring the remainder
Example 27 / 5 = 5
"""


def solution1(numerator, denominator):
    
    if numerator < denominator:
        return 0

    return solution1((numerator - denominator), denominator) + 1

def solution2(numerator, denominator):
    counter = 0
    while numerator > denominator:
        numerator = numerator - denominator
        counter = counter + 1
        #else:
        #break

    return counter


print(solution1(27, 5))
print(solution2(2000007, 5))
