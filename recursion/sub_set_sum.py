"""
count number of subsets that sum to k
"""

def subsetsum(S, K):
    return shelper(S, 0, K, [], 0)

def shelper(S, i, K, slate, slatesum):
    if slatesum > K:
        return 0
    if slatesum == K:
        return 1
    if i == len(S):
        return 0
    else:
        return shelper(S, i+1, K, slate, slatesum) + shelper(S, i+1, K, slate+[S[i]], slatesum+S[i])

print(subsetsum([1,2,3,4,5], 4))
