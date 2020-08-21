"""
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution:
    def plus_one(self, digits):
        digit_len = len(digits) 
        j = digit_len - 1
        #for i in range(digit_len):
        #edge case
        if digit_len == 0:
            return digits

        value = digits[j] + 1
        if value == 10:
            digits[j] = 0
                
            if j == 0:
                digits.insert(0, 1)
                return digits

            j = j - 1
            while j >= 0:
                if digits[j] + 1 == 10:
                    digits[j] = 0
                    if j == 0:
                        digits.insert(0, 1)
                        return digits
                else:
                    digits[j] = digits[j] + 1
                    return digits
                j = j - 1
        else:
            digits[j] = digits[j] + 1

        return digits

sol = Solution()
print("The solution is: ", sol.plus_one( [1,2,3] ))
print("The solution is: ", sol.plus_one( [4,3,2,1])) 
print("The solution is: ", sol.plus_one( [9])) 
print("The solution is: ", sol.plus_one( [8])) 
print("The solution is: ", sol.plus_one( [])) 
print("The solution is: ", sol.plus_one( [9,9])) 
print("The solution is: ", sol.plus_one( [9,0,9] ))



                    
            


