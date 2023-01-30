"""combinatorial sequence is not always built out of numbers

    Returns:
        _type_: _description_
    """
class Solution:
    def generate_paranthesis(self, n):
        result = []

        def helper(numleft, numright, slate):
            if numleft > numright or numleft < 0 or numright < 0:
                return

            # base case
            if numleft == numright == 0:
                result.append("".join(slate))
                return

            #recursive case
            #include ()
            slate.append('(')
            helper(numleft-1, numright, slate)
            slate.pop()

            #include )
            slate.append(')')
            helper(numleft, numright-1, slate)
            slate.pop()

        helper(n, n, [])
        return result

sol = Solution()
print(sol.generate_paranthesis(4))
