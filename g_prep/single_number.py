"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution0:
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

class Solution:
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a = a ^ i

        return a
sol = Solution()
print("The solution is: ", sol.singleNumber([2,2,1])) 
print("The solution is: ", sol.singleNumber([4,1,2,1,2])) 
