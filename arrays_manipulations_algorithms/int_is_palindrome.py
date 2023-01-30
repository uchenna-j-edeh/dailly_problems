from math import pow
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x == 0:
            return True

        # store in a list and process further
        store = list()
        while  x >= 1: # True, True, False
            reminder = x %  10  # 1 = 121 % 10, 1 = 12/10, 1//10
            x = x // 10 # 12 = 121 // 10, 1, 0
            store.append(reminder) # 1, 2, 1
 
        j = len(store) - 1
        half = len(store) // 2
        for i in range(len(store)):
            if store[i] != store[j]:
                return False
            if i == half:
                return True
            j = j - 1


solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))
print(solution.isPalindrome(11))
print(solution.isPalindrome(0))
