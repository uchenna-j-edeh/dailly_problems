"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution:
    def moveZeroes(self, nums):
        nums_len = len(nums)
        if nums_len == 0 or nums_len == 1:
            return nums

        for i in range(nums_len):
            j = i + 1
            #import pdb; pdb.set_trace()
            while j < nums_len:
                if nums[i] == 0 and nums[i] == nums[j]:
                    # advance
                    j = j + 1
                elif nums[i] == 0 and nums[i] != nums[j]:
                    # swap
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
                else:
                    break

        return nums

sol = Solution()
print("The solution is: ", sol.moveZeroes([1, 0]))
print("The solution is: ", sol.moveZeroes([0,1,0,3,12]))
print("The solution is: ", sol.moveZeroes([0,1]))
print("The solution is: ", sol.moveZeroes([1]))
print("The solution is: ", sol.moveZeroes([]))

