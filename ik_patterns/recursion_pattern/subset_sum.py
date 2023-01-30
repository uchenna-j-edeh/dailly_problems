"""subset sum equal a certain number. 
backatrack case
if sum(slate) > c:
    return
elif sum(slate) ==:
    result.append(slate[:])
    return

# base case
if i == len(s):
    #add to the bag
# recursive case

# count all with sum equals to a certain number. instead of a global bag, we have global count
elif sum(slate) ==:
    result +=
    return

prune as much as possible as higher up as possible
    """

class Solution:
    def back_track(self, s, k):
        result = []
        def helper (s, i, k, slate):
            if i == len(s):
                result.append(slate[:])
                return

            # backtrack case
            if sum(slate) == k:
                result.append(slate[:])
                return

            if sum(slate) > k and sum(slate) < k:
                return

            # recursion case
            # exclusion case
            helper(s, i+1, k, slate)

            # exclusion case
            slate.append(s[i])
            helper(s, i+1, k, slate)
            slate.pop()

        helper(s, 0, k, [])
        return result

# sol = Solution()
# k = 2
# n = 4
# s = [i for i in range(1, n+1)]
# print(sol.back_track(s, k))
