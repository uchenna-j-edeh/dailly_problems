"""
sometimes we can evaluate the partially constructed solution to a combinatorial search problem: if none of the ways to fill in the remaining
blanks can lead to a solution( or if we can directly identify the one single solujtion that will emerge), we do not need to work to fill in the remaining blanks

insteas, we bactrack from that internal node, thus prune away the subtree rooted at it.

tbhough it leads to exponential improvements to combiatorial search, the resulting time is not polynomial improvement in combniatorial the resulting
time is not polynomial, but an improved exponential time. i.e difficult to give an exact expression for the time comokexity.
It is best treated as heuristic than something amenable to worst-casr analysis
It allows you to prune away subtrees.

77. Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.


Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:

1 <= n <= 20
1 <= k <= n
"""

class Solution:
    def back_track(self, s, k):
        result = []
        def helper (s, i, k, slate):
            if i == len(s):
                result.append(slate[:])
                return

            # backtrack case
            if len(slate) == k:
                result.append(slate[:])
                return

            if len(slate) > k:
                return

            # recursion case
            # exclusion case
            helper(s, i+1, k, slate)

            # exclusion case
            slate.append(s[i])
            helper(s, i+1, k, slate)
            slate.pop()

        helper(s, 0, k, [])
        return result

sol = Solution()
k = 2
n = 4
s = [i for i in range(1, n+1)]
print(sol.back_track(s, k))
