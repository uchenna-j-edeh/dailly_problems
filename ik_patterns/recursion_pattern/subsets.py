"""leetcode 78
78. Subsets
Medium
13.2K
187
company
Amazon
company
Bloomberg
company
Facebook
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

class Solution(object):
    def subsets(self, num):
        result = []
        def helper(s, i, slate):
            if i ==len(s):
                result.append(slate)
                return

            helper(s, i+1, slate) # Exlusion
            helper(s, i+1, slate + [s[i]]) # inclusion

        helper(num, 0, [])

        return result

sol = Solution()
print(sol.subsets("123"))