# -*- coding: utf-8 -*-
"""
Author:https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
A permutation, also called an “arrangement number” or “order,” is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. A string of length n has n! permutation.
Source: Mathword(http://mathworld.wolfram.com/Permutation.html)

Below are the permutations of string ABC.
ABC ACB BAC BCA CBA CAB
"""
# Python program to print all permutations with
# duplicates allowed

def toString(List):
    return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print(toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack # Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
#def permute(a, l, r):
#    if l==r:
#        print(toString(a))
#    else:
#        for i in range(l,r+1):
#            a[l], a[i] = a[i], a[l]
#            permute(a, l+1, r)
#            a[l], a[i] = a[i], a[l] # backtrack


#string = "ABCDEFG"
#_str = 'UCHENA'
_str = 'UCHE'
n = len(_str) 
a = list(_str) 
permute(a, 0, n-1) 
