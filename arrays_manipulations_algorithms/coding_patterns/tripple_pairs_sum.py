"""Triplet Sum
Medium
Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 .
The solution must not contain duplicate triplets 
(e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates).
If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [[-3, 1, 2], [-1, 0, 1]]

Transform the data by sorting. 
Then use the pair sum and find 2 pairs that sum up to negative of first pair from right
"""

def pair_sum_sort(mlist, target):
    """_summary_

    Args:
        mlist (_type_): _description_
        mtarget (_type_): _description_

    Returns:
        _type_: _description_
    """
    mtarget = target
    # mtarget *= -1

    j = len(mlist) - 1
    # for i in range(len(mlist)):
    i = 0
    result = []
    # print(mlist)
    # print(target)
    # print(mtarget)
    while (j > i): # 3 > 0
        sum_pairs = mlist[i] + mlist[j] # -1+2=1, 0+2=2, 1+2=3
        if sum_pairs < mtarget: # 1 < 3, 2 < 3, *
            i += 1
        elif sum_pairs > mtarget:# *,*,*
            j -= 1

        else: # 3=3
            # print(target)
            # print(mlist[i])
            if target == mlist[i]: # 3 == 2
                return [] # another dups
            result.append(i)
            result.append(j)
            return result

    return result

def triple_pairs_sum_func(args_list):
    """_summary_

    Args:
        args_list (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = []
    args_list = sorted(args_list) # [-3, -1, 0, 1, 2]
    for i in range(len(args_list)):
        if i > 0 and args_list[i] == args_list[i-1]:
            continue # avoid dubplicates

        if args_list[i] > 0: # all positve numbers can't sum to zero
            return result

        target = -1 * args_list[i]
        res = pair_sum_sort(args_list[i+1:], target)
        # print(f'result: {result}')
        if len(res) > 0:
            result.append([i, res[0], res[1]])
    return result


print(triple_pairs_sum_func( [0, -1, 2, -3, 1]))