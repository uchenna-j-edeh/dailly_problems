"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


Example 1:

Input: nums = [1,2,3]
Output: [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
    ]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

Strategy:
every permutation is a seq of lenth n. Basically a re-ordering
"""

class Solution:
    def permute(self, nums):
        result = []
        def helper(s, i, slate):
            #base case
            if i == len(s):
                result.append(slate[:])
                return

            # recursive case
            for pick in range(i, len(s)):
                s[i], s[pick] = s[pick], s[i]
                slate.append(s[i])
                helper(s, i+1, slate)
                slate.pop()
                s[i], s[pick] = s[pick], s[i]

        helper(nums, 0, [])
        return result



sol = Solution()
print(sol.permute(['1','2','3','4']))
