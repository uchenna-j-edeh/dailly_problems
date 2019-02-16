"""
Reverse half array.
Example: 'abcdefghijklmnopqrstuvwxyz' would be 'abcdefghijklmnzyxwvutsrqpo'
"""

def solution1(text):
    len_list = len(text)//2
    #print(text[:len_list])
    #print(text[len_list:])
    
    new_str = ''
    for tx in text[len_list:]:
        new_str = tx + new_str

    return text[:len_list] + new_str

print(solution1('abcdefghijklmzyxwvutsrqpon'))
