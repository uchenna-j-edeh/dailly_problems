"""
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
class Solution:
    def subsets(self, nums):
        result = []
        #Solution using mutable slate
        def generate_count(slate, i):
            count = 1
            for j in range(i, len(slate)):
                if slate[j] == slate[i]:
                    count += 1
                else:
                    return count

        def helper(s, i, slate):
            if i == len(s):
                result.append(slate[:])
                return

            # recursive case
            #Exclude s[i]

            count = generate_count(slate, i)
            helper(s, i + count, slate)

            #Include s[i]
            for i in range(1, count):
                slate.append(s[i])
                helper(s, i + count, slate)

            for i in range(i, count):
                slate.pop()

        nums = sorted(nums)
        helper(nums, 0, [])
        return result

sol = Solution()
print(sol.subsets("121"))
