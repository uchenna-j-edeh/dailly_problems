"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.


Note: You may assume the string contains only lowercase English letters.
"""

class Solution:
    def firstUniqChar(self, s):
        sdict = dict()

        for i in s:
            if not sdict.get(i, False):
                sdict[i] = 1
            else:
                sdict[i] = sdict[i] + 1

        for j in range(len(s)):
            if sdict[s[j]] == 1:
                return j
        
        return -1

sol = Solution()
print("The solution is: ", sol.firstUniqChar("leetcode"))
print("The solution is: ", sol.firstUniqChar("loveleetcode"))


