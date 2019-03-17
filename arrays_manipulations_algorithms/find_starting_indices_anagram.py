"""
Author: Uchenna Edeh
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

def solution(S, W):
    indices = []
    len_w = len(W)
    rw = ''.join(reversed(W))  
    for i, _ in enumerate(S):
        j = i + len(W)
        pattern = S[i:j]

        if pattern == W:
            indices.append(i)

        elif pattern == rw:
            indices.append(i)

    return indices

print(solution('abxaba', 'ab'))


