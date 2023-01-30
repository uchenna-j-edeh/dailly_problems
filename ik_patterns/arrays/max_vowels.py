"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""
def check_vowels_count(win):
    vowels = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
    count = 0
    for i in win: # abc
        if vowels.get(i, False):
            count +=1

    return count # 1

def max_vowels_k(s, k): # "abciiidef"
    # window = s[0:k] # abc
    # max_count = check_vowels_count(window) # abc, return 1
    max_count = 0
    for i in range(k, len(s)):
        window = s[i-k:i]
        count = check_vowels_count(window)
        if count > max_count:
            max_count = count

    return max_count

s = "abciiidef"
k = 3
print(max_vowels_k(s, k))
