"""
Reverse half array.
Example: 'abcdefghijklmnopqrstuvwxyz' would be 'abcdefghijklmnzyxwvutsrqpo'
"""

def solution1(text):
    len_list = len(text)//2
    print(len_list)
    quater = len(text[:len_list])//2
    print(text[quater])
    print(text[len_list])


print(solution1('abcdefghijklmnopqrstuvwxyz'))
