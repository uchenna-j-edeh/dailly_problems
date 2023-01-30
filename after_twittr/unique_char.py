"""
Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?
example: input: 'uchenna'
output: false
"""

def is_unique_char(text):
    #assuming it's ascii char which is 256 characters
    my_list = []
    for i in range(256):
        my_list.append(0)

    for t in text:
        if my_list[ord(t)] == 1:
            return False
        my_list[ord(t)] = my_list[ord(t)] + 1

    return True

print(is_unique_char('Uchenna'))
print(is_unique_char('Samuel'))

