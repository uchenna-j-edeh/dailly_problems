"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""

class Solution:
    def swap(self, i, j, arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        return arr

    def reverseString(self, s):
        s_len = len(s)
        end = s_len // 2

        j = s_len - 1
        for i in range(s_len):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            if i == end - 1:
                return s
            j = j - 1

sol = Solution()
print("Solution is: ", sol.reverseString(["h","e","l","l","o"]))
print("Solution is: ", sol.reverseString(["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]))
print("Solution is: ", sol.reverseString(["H","a","n","n","a","h"]))



