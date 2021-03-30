"""
Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
"""

def solution(astr, pattern):
    """sliding window"""
    j = len(pattern) # 3
    result = []
    for i in range(len(astr)):
        if j < len(astr) and astr[i:j] == pattern:
            result.append(i)
        j = j+1 # 0+3| 1+4| 2+5
    return result

print(solution("abracadabra", "abr"))
