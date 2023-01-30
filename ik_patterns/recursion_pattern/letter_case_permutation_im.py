class Solution(object):
    def letterCasePermutation(self, S):
        """_summary_

        Args:
            S (_type_): _description_
        """
        result = []
        def helper(S, i, slate):
            if i == len(S):
                result.append(slate)
            else:
                if S[i].isdigit():
                    helper(S, i+1, slate+S[i])
                else:
                    helper(S, i+1, slate+S[i].upper())
                    helper(S, i+1, slate+S[i].lower())

        helper(S, 0, "")

        return result

sol = Solution()
print(sol.letterCasePermutation("a1b2"))