"""
Author: Uchenna Edeh
Given a list of integers and a number K, return contiguous elements of the list sum to k.

Example, if the list is [1,2,3,4,5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

def solution(mylist, k):
    sum_seq = 0
    seq = []
    for val in mylist:
        seq = seq + [val]
        sum_seq = sum_seq + val
        if sum_seq > k:
            # try removing first, elem,then second, until less than l
            for i, sq in enumerate(seq):
                if sum_seq - sum(seq[0:i]) == k:
                    return seq[i:]
                if sum_seq - sum(seq[0:i]) < k:
                    sum_seq = sum_seq - sum(seq[0:i])
                    seq = seq[i+1:]

print(solution([1,2,3,4,5,45], 50))
#print(solution([1,2,3,4,5], 7))
#print(solution([1,2,3,4,5], 9))
