"""
Author: Uchenna Edeh
Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.
For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""

def solution(lst):
    if not isinstance(lst, list):
        raise ValueError("Data is not a valid list data type...")

    if not len(lst):
        raise ValueError("List data used is empty...")

    i = 0
    len_lst = len(lst)
    prev_idx = len_lst
    while(True):
        hop = lst[i]
        if not isinstance(hop, int):
            raise ValueError("Invalid data type found in list...")
        if prev_idx == i:
            return False
        if (i + hop) > len_lst - 1:
            return False
        if (i + hop) == len_lst - 1:
            return True

        prev_idx = i
        i = i + hop

print(solution([2, 0, 1, 0]))
print(solution([1, 1, 0, 1]))
print(solution([1, 1, 0, 1, 1, 3, 0, 0 , 1]))
print(solution([1, 2, 0, 1, 1, 3, 0, 0 , 1, 0]))


