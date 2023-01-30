"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.
 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

Strategy:
for n choose k problems, it always fill in a series of blanks
this series of blankls denotes a combination/permutation of differnt objects
you proceed from left to right as a lazy manager only take responsibility for filling in the first blank, then delegate the rest of the work to subordinates
skeleton:
function helper(partial soln, sub problem feinition)
    # base case
    if sub problem == 0:
        #partial sol is complete 
        return

    # recursion case
    # choices: c1,....ck
    # inclusion case ( append )                           | exclusion case
    helper(partial sol + c, slightly smaller problem def) | helper(sol, smaller sub prob)

function overall problem(set of objects n):
    result = [] # bags
    helper (empty slate, overal problem size n)
    return
"""
import copy
class Solution(object):
    def letter_case(self, s):


        result = []
        def helper(s, i, slate):
            # base condition
            if i == len(s):
                # state = copy.deepcopy(slate)
                result.append("".join(slate))
                return

            # recursive case
            #left  | right
            if s[i].isdigit():
                slate.append(s[i])
                helper(s, i+1, slate)
                slate.pop()

            elif s[i].isalpha():
                slate.append(str(s[i].lower()))
                helper(s, i+1, slate)
                slate.pop()

                slate.append(str(s[i].upper()))
                helper(s, i+1, slate)
                slate.pop()

        helper(s, 0, [])
        return result

sol = Solution()
print(sol.letter_case(['a', 'i', 'b', '2']))


