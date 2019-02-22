"""
Calculate the GCD of a number.
Algorithim: Euclid
"""

import sys

def euclidGCD(a, b):
    if b == 0:
        return a
    remainder = a % b
    return euclidGCD(b, remainder)

if __name__ == "__main__":
    _in = input("Enter a number. Example 20 4:")
    a, b = map(int, _in.split())
    gcd = euclidGCD(a, b)
    lcm = (a * b) / gcd

    print("GCD => {0}, LCM = > {1}".format(gcd, lcm))
    
