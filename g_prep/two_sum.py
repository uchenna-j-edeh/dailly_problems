"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        nums_dicts = dict()

        for i, v in enumerate(nums):
            nums_dicts[v] = i
        print(nums_dicts)
        for k, j in enumerate(nums):
            diff = target - j
            # becasue we cannot use the same indice twice and solution is guranteed to be two, there is no chance to test indice, i = 0
            if nums_dicts.get(diff, False):
                value = nums_dicts[diff] 
                if k != value:
                    return [k, value]

        return []

sol = Solution()
print("The solution is: ", sol.twoSum([2, 7, 11, 15], 9))
print("The solution is: ", sol.twoSum([1, 3, 4, 2], 6))
