"""
    Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

def is_palindrom(input):

    i = 0
    j = len(input) - 1

    is_odd = len(input) % 2 == 1
    is_even = len(input) % 2 == 0
    is_valid = False
    if is_odd:
        while (i - j < 2):
            if not(input[i] == input[j]):
                return False
            i = i + 1
            j = j - 1

    else:
        while (i - j-1 < 1):
            if not(input[i] == input[j]):
                return False
            i = i + 1
            j = j - 1
    return True

# print(is_palindrom("bab"))
# print(is_palindrom("bb"))
# print(is_palindrom("bcb"))
# print(is_palindrom('enna'))

def check_palindrome(input):

    i = 0
    j = 2
    max_palindrome = ''
    curr = ''
    len_input = len(input) 
    while(len_input - i > 2):
    # for i in range(len(input)):
        if is_palindrom(input[i:j]):
            j = j + 1
            curr = input[i:j]
        else:
            i = i + 1
            j = i + 2
            if len(curr) > len(max_palindrome):
                max_palindrome = curr

    
input = "babab"
print(check_palindrome(input))


        




