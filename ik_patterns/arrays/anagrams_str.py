"""
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

def is_anagram(s,p):
    s_map = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'j':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,
        'o':0,
        'p':0,
        'q':0,
        'r':0,
        's':0,
        't':0,
        'u':0,
        'v':0,
        'w':0,
        'x':0,
        'y':0,
        'z':0
    }
    p_map = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'j':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,
        'o':0,
        'p':0,
        'q':0,
        'r':0,
        's':0,
        't':0,
        'u':0,
        'v':0,
        'w':0,
        'x':0,
        'y':0,
        'z':0
    }
    #  initilization
    for k in p:
        if p_map.get(k, False):
            p_map[k] += 1
        else:
            p_map[k] = 1

    k = len(p)
    window = s[0:k]
    results = []
    for j in window:
        if s_map.get(j, False):
            s_map += 1
        else:
            s_map[j] = 1


    if s_map == p_map:
        results.append(0)

    for i in range(k, len(s)):

        # remove index i-k
        s_map[s[i-k]] -= 1

        # inser index i
        s_map[s[i]] += 1

        if s_map == p_map:
            results.append(i-k+1)

    return results


s = "cbaebabacd"
p = "abc"
# output [0, 6]

print(is_anagram(s, p))

s = "abab"
p = "ab"
print(is_anagram(s, p))
# Output: [0,1,2]



