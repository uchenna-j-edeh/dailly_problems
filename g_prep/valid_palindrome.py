"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


Constraints:

s consists only of printable ASCII characters.
"""
class Solution:
    def isPlaindrome(self, s):
        word_len = len(s)
        i = 0
        j = word_len - 1
        if word_len == 2:
            if s[0].isalpha() and s[1].isalpha():
                return s[0].lower() == s[1].lower()
            else:
                return True

        while( i < j):
            #print('i => ', s[i], 'j=>', s[j])
            if s[i].isalpha() and s[j].isalpha():
                if s[i].lower() == s[j].lower():
                    i = i + 1
                    j = j - 1
                else:
                    return False
            elif s[i].isalpha():
                j = j - 1
            elif s[j].isalpha():
                i = i + 1
            else:
                i = i + 1
                j = j - 1

        return True



sol = Solution()
print("The solution is: ", sol.isPlaindrome("A man, a plan, a canal: Panama"))
print("The solution is: ", sol.isPlaindrome("race a car"))
print("The solution is: ", sol.isPlaindrome("race a car"))
print("The solution is: ", sol.isPlaindrome("OP"))
print("The solution is: ", sol.isPlaindrome("a."))
