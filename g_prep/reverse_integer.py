"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
import math
class Solution:
    def digitCounter(self, num):
        count = 0
        while(num > 0):
            num = num // 10
            count = count + 1
        return count

    def reverse(self, x):
        overflow = math.pow(2, 31) - 1 
        underflow = -1 * overflow

        #digit_count = self.digitCounter(x)
        is_negative = x < 0

        total = 0
        if x < 1:
            x = -1 * x

        digit_count = self.digitCounter(x)
        print(x)
        while x > 0:
            digit = x % 10

            total = math.pow(10, digit_count - 1) * digit + total
            x = x//10
            digit_count = digit_count - 1

            if total > overflow or total < underflow:
                return 0

        if is_negative:
            total = -1 * total

        return int(total)

sol = Solution()
print("The solution is: ", sol.reverse(123)) 
print("The solution is: ", sol.reverse(-123)) 
print("The solution is: ", sol.reverse(120)) 

        
