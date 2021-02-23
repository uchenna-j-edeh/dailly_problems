"""
Given a string S, we can transform every letter individually to lowercase or uppercase to create another string. Return a list of all possible strings we could create.


Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Algo;
1. Read each character
2. if digit, then you remember/store it
2. if letter, then consider 2 choices:
    a. remember|store lower case character
    b. remember|store uppper case character


"""
#solution with mutatble parameter
class Solution(object):
    def letterCasePermutation(self, S):
        result = []

        def helper(S, i, slate):
            if i ==len(S):
                result.append("".join(slate))
                return

            if S[i].isdigit():
                slate.append(S[i])
                helper(S, i+1, slate)
                slate.pop()
            else:
                slate.append(S[i].lower())
                helper(S, i+1, slate)
                slate.pop()
                slate.append(S[i].upper())
                helper(S, i+1, slate)
                slate.pop()
        
        helper(S, 0, [])
        return result

sol = Solution()
print(sol.letterCasePermutation("a1b2"))


#using class object:
class PermuteLetter(object):
    def __init__(self):
        self.result = []

    def helper(self, s, i, slate):
        # base case
        if i == len(s):
            self.result.append(slate)
            return

        # recursive case
        if s[i].isdigit():
            self.helper(s, i + 1, slate + s[i])
        else:
            self.helper(s, i + 1, slate + s[i].lower())

            self.helper(s, i + 1, slate + s[i].upper())


def helper(s, i, slate, result):
    # base case
    if i == len(s):
        result.append(slate)
        return 

    # recursive case
    if s[i].isdigit():
        helper(s, i + 1, slate + s[i], result)
    else:
        helper(s, i + 1, slate + s[i].lower(), result)

        helper(s, i + 1, slate + s[i].upper(), result)


def permute_letter(mletter):
    result = []
    helper(mletter, 0, "", result)
    return result

def permute_letter_v2(letters):
    PL = PermuteLetter()
    PL.helper(letters, 0, "")
    return PL.result


print(permute_letter('a1b2'))
print(permute_letter_v2('cde1'))


