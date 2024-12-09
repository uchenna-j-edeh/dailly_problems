"""Is Palindrome Valid
Easy
A palindrome is a sequence of characters that reads the same forward and backward.

Given a string, determine if it's a palindrome after removing all non-alphanumeric characters. A character is alphanumeric if it's either a letter or a number.

Example 1:
Input: s = 'a dog! a panic in a pagoda.'
Output: True
Example 2:
Input: s = 'abc123'
Output: False
Constraints:
The string may include a combination of lowercase English letters, numbers, spaces, and punctuations.
"""

def solve_palindrome(text): # 'a dog! a panic in a pagoda.'
    """_summary_

    Args:
        text (_type_): _description_

    Returns:
        _type_: _description_
    """

    j = len(text) - 1
    i = 0
    while j !=  i:
        if not text[i].isalnum():
            i += 1

        elif not text[j].isalnum():
            j -= 1

        elif text[i] == text[j]:
            i += 1
            j -= 1

        else:
            return False # we encounter charater on both side that are not same. hence, will never be palindome

    return True

print(solve_palindrome('a dog! a panic in a pagoda.'))
print(solve_palindrome('abc123'))


