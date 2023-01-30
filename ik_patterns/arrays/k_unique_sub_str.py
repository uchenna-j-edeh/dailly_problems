"""
1100. Find K-Length Substrings With No Repeated Characters

Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

 

Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
1 <= k <= 104
    """
def is_unique_sub_str(sub_str):
    mydict = {}
    for j in sub_str:#"havef
        if mydict.get(j, False):
            return False
        mydict[j] = 1
    return True
def unique_sub_str(s, k): # "havefunonleetcode"
    count = 0
    for i in range(k, len(s)+1): # "havef # last index would be 16, but to get the last char we need s[12:17]
        window = s[i-k:i] # "havef, avefu
        status = is_unique_sub_str(window)
        if status: # true, true
            count += 1 # 2

    return count

s = "havefunonleetcode"
k = 5
print(unique_sub_str(s, k))