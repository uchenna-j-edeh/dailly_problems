"""
    Pair Sum - Sorted
Easy
Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers in the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example 1:
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
Explanation: nums[2] + nums[3] = 3 + 4 = 7

Example 2:
Input: nums = [1, 1, 1], target = 2
Output: [0, 1]
Explanation: other valid outputs could be [1, 0], [0, 2], [2, 0], [1, 2] or [2, 1].
"""

def pair_sum_sort(mlist, mtarget):
    j = len(mlist) - 1
    # for i in range(len(mlist)):
    i = 0
    result = []
    while (j > i):
        sum_pairs = mlist[i] + mlist[j]
        if sum_pairs < mtarget:
            i += 1
        elif sum_pairs > mtarget:
            j -= 1

        else:
            result.append(i)
            result.append(j)
            return result

    return result
print(pair_sum_sort([-5, -2, 3, 4, 6], 7))
print(pair_sum_sort([],0))