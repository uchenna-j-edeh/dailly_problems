"""
Author: Uchenna Edeh
Given two sorted lists, return a list of their intersection with no duplicates with O(1) space and O(n) runtime.
For example: A = [2, 3, 3, 4, 6, 6, 8], B = [3, 3, 6, 7, 9] should return [3, 6]
"""


def solution1(listA, listB):
    len_a = len(listA)
    len_b = len(listB)

    intersection = set()

    longer_list = None
    shorter_list = None
    if len_a > len_b:
        longer_list = listA
        shorter_list = listB
    else:
        longer_list = listB
        shorter_list = listA

    j = 0
    for i, val_a in enumerate(longer_list):
        #import pdb; pdb.set_trace()
        if j < len(shorter_list):
            if longer_list[i] > shorter_list[j]:
                for k in range(j+1, len(shorter_list[j])):
                    if shorter_list[k] == longer_list[i]:
                        intersection.add(longer_list[k])
                        j = 1 + j
                    if longer_list[i] > shorter_list[k]:
                        j = 1 + i
                
                    if longer_list[i] < shorter_list[k]:
                        break
            if longer_list[i] ==  shorter_list[j]:
                intersection.add(longer_list[i])
                j =  1 + i
        else:
            return intersection

    return intersection

A =  [2, 3, 3, 4, 6, 6, 8]
B = [3, 3, 6, 7, 9]

print(solution1(A, B))
