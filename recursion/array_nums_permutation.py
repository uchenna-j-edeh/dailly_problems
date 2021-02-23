"""
Given [1,2,3], find all it's permutations...
"""

def helper(S, i, slate, result):
    if i == len(S): # base case
        result.append(slate[:])
        #print(slate[:])
        return

    # recursive case
    for p in range(i, len(S)):
        S[p], S[i] = S[i], S[p]
        slate.append(S[i])
        helper(S, i + 1, slate, result)
        slate.pop()
        S[p], S[i] = S[i], S[p]


def generate_permutation(nums):
    result = []
    helper(nums, 0, [], result)
    return result


print(generate_permutation([1,2,3]))
print(generate_permutation([1,2,1]))

#################################################
def helper_uq(S, i, slate, result):
    if i == len(S): # base case
        result.append(slate[:])
        #print(slate[:])
        return

    # recursive case
    mhash = dict()
    for p in range(i, len(S)):
        if not mhash.get(S[p], False):
            mhash[S[p]] = True
            S[p], S[i] = S[i], S[p]
            slate.append(S[i])
            helper_uq(S, i + 1, slate, result)
            slate.pop()
            S[p], S[i] = S[i], S[p]



def generate_permutation_unique(nums):
    result = []
    helper_uq(nums, 0, [], result)
    return result

print(generate_permutation_unique([1,2,1]))
