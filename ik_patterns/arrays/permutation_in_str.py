"""567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
Accepted
538.6K
Submissions
1.2M
Acceptance Rate
43.5%
Seen this question in a real interview before?
1/4
Yes
No
"""



def permute_str(s1,s2):
    if s1 > s2:
        return False
    s1_map = {
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
    for s in s1:
        if s1_map.get(s, False):
            s1_map[s] +=1
        else:
            s1_map[s] = 1 

    k = len(s1)

    s2_map = {
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
    window = s2[0:k]

    for i in window:
        if s2_map.get(i, False):
            s2_map[i] +=1
        else:
            s2_map[i] = 1
    
    if s1_map == s2_map:
        return True
    # consider next index
    
    for j in range(k, len(s2)): # eidbaooo
        s2_map[s2[j-k]] = s2_map[s2[j-k]] - 1 # j-k => 3 - 2, 4 - 2, 
        # s2_map = compare_s1_s2(window)
        s2_map[s2[j]] =  s2_map[s2[j]] + 1

        if s2_map == s1_map:
            return True

    return False


# Example 1:

s1 = "ab"
s2 = "eidbaooo"
print(permute_str(s1, s2))
# Example 2:

s1 = "ab"
s2 = "eidboaoo"
print(permute_str(s1, s2))