"""47. Permutations II
Medium
6.9K
125
company
Amazon
company
Microsoft
company
LinkedIn
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
strategy:
naive way: build all the trees and at the end check
smarter way, identify worker doing the same work and not build the sub tree.
so when i am picking element, just pick only ones that has not been picked before
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
                hmap = {}
                if not hmap.get(pick, False):
                    hmap[pick] = 1
                    s[i], s[pick] = s[pick], s[i]
                    slate.append(s[i])
                    helper(s, i+1, slate)
                    slate.pop()
                    s[i], s[pick] = s[pick], s[i]

        helper(nums, 0, [])
        return result



sol = Solution()
print(sol.permute(['1','2','3','1']))