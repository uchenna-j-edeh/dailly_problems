"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def isAnagram(self, s, t):
        s_word_len = len(s)
        t_word_len = len(t)
        if s_word_len != t_word_len:
            return False

        letters = "abcdefghijklmnopqrstuvwxyz"
        ascii_form = []
        for i in letters:
            ascii_form.append(0)

        for j in s:
            indx = ord(j) - ord('a')
            ascii_form[indx] = ascii_form[indx] + 1

        for k in t:
            indx = ord(k) - ord('a')
            ascii_form[indx] = ascii_form[indx] - 1

        for t in ascii_form:
            if t:
                return False
        return True



sol = Solution()
print("The Solution is: ", sol.isAnagram("anagram", "nagaram"))
print("The Solution is: ", sol.isAnagram("rat", "car"))


            
