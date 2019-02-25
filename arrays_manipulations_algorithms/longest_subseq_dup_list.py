"""
Author: Uchenna Edeh
The longest subsequence of duplicate in list. Eg. input: 1,5,9,1,1,1,0. Output: 1,1,1,1
wikipedia: In mathematics, a subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. For example, the sequence { A,B,D} is a subsequence of {A,B,C,D,E,F} obtained after removal of elements C, E, and F. The relation of one sequence being the subsequence of another is a preorder.
"""

def solution1(mylist):
    mhash = dict()
    max_elem = 0
    max_count = 0
    for i, val in enumerate(mylist):
        if mhash.get(val, False):
            hval = mhash[val]
            mhash[val] = hval + 1
        else:
            mhash[val] = 1

    for val in mhash.keys():
        if mhash[val] > max_count:
            max_elem = val
            max_count = max_elem

    
    return [max_elem for x in range(mhash[max_elem])]

print(solution1([1,5,9,1,1,1,0]))



