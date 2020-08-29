"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

class Solution:
    def isValid(self, s):
        stack1 = []
        is_valid = False
        s_len = len(s)

        # edge case
        if s_len == 0:
            return True

        if s_len % 2: # optimization
            return False

        for i in range(s_len):
            j = s_len - i - 1
            if s[j] == ']' or s[j] == '}' or s[j] == ')':
                stack1.append(s[j])
            else:
                if not len(stack1):
                    return False
                result = stack1.pop()
                if s[j] == '{' and result == '}' \
                        or s[j] == '[' and result == ']' \
                        or s[j] == '(' and result == ')':
                            is_valid = True
                else:
                    return False


        return is_valid


sol = Solution()
print("The solution is: ", sol.isValid("()"))
print("The solution is: ", sol.isValid("()[]{}"))
print("The solution is: ", sol.isValid("(]"))
print("The solution is: ", sol.isValid("([)]"))
print("The solution is: ", sol.isValid("{[]}"))
print("The solution is: ", sol.isValid("}"))
print("The solution is: ", sol.isValid(""))
print("The solution is: ", sol.isValid("]"))
print("The solution is: ", sol.isValid("(("))

        

