"""
Author: Uchenna Edeh
Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""
import random

def solution(n, l):
    if not isinstance(n, int):
        raise ValueError("Type must be an integer...")

    if not isinstance(l, list):
        raise ValueError("Type must be a list to continue...")
    
    if n < 0:
        raise ValueError("Integer value must be non-negative...")

    
    rand_int = random.randint(0, n-1)
    mhash = dict()
    for h in l:
        if not isinstance(h, int):
            raise ValueError("List must contain a valid integer element...")
        mhash[h] = 1

    while(mhash.get(rand_int, False)):
        rand_int = random.randint(0, n-1)

    return rand_int

#print(solution(20, [2, 5, 9, 12]))
print(solution(30, [2, 5, 9, 12, 25, 27, 28, 29]))
