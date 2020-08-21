"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def findMatch(self, sub_str, word):
        a_match = ""
        short_str = len(sub_str)
        long_str = len(word)

        if short_str > long_str:
            temp = short_str
            short_str = long_str
            long_str = temp
            #import pdb; pdb.set_trace()
        for i in range(short_str):
            if i == 0 and sub_str[i] != word[i]:
                break

            if sub_str[i] == word[i]:
                a_match = a_match + word[i]
            else:
                #print(a_match)
                return a_match 
        #print(a_match)
        return a_match
        

    def longestCommonPrefix(self, strs):
        strs_len = len(strs)
        if strs_len == 0 or strs_len == 1:
            return ""

        sub_str = self.findMatch(strs[0], strs[1])
        if len(sub_str) == 0:
            return ""

        for i in range(1, strs_len):
            #print(i)
            if i + 1 < strs_len:
                sub_str = self.findMatch(sub_str, strs[i+1])
                if len(sub_str) == 0:
                    return ""
        
        return sub_str

sol = Solution()
print("The solution is: ", sol.longestCommonPrefix(["flower","flow","flight"]))
print("The solution is: ", sol.longestCommonPrefix(["flower","flow"]))
print("The solution is: ", sol.longestCommonPrefix(["flower","flight","flow"]))
print("The solution is: ", sol.longestCommonPrefix(["dog","racecar","car"]))

                

