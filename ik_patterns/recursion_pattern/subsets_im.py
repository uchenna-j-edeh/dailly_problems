class Solution:
    def subsets(self, nums):
        result = []
        #Solution using mutable slate
        def helper(s, i, slate):
            if i == len(s):
                result.append(slate[:])
                return

            # recursive case
            #Exclude s[i]
            helper(s, i+1, slate)
            #Include s[i]

            slate.append(s[i])
            helper(s, i+1, slate)
            slate.pop()

        helper(nums, 0, [])
        return result

sol = Solution()
print(sol.subsets("123"))

