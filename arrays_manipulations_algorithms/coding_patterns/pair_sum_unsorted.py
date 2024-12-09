"""Pair Sum - Unsorted
Easy
Given an array of integers, return the indexes of any two numbers that add up to a target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example:
Input: nums = [-1, 3, 4, 2], target = 3
Output: [0, 2]
Explanation: nums[0] + nums[2] = -1 + 4 = 3

Constraints:
The same index cannot be used twice in the result.
"""

def paired_sum_unsorted_func(mlist, target):
    """_summary_

    Args:
        mlist (_type_): _description_
        target (_type_): _description_

    Returns:
        _type_: _description_
    """
    mdict = {}
    for i, v in enumerate(mlist):
        mdict[v] = i

    for i, v in enumerate(mlist):
        complement = target - v
        if mdict.get(complement, False) and i != mlist[v]:
            return [i, mlist[v]]

    return []


print(paired_sum_unsorted_func([-1, 3, 4, 2], 3))
