"""
The Challenge
In this exercise, you're going to decompress a compressed string.

Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

The input

3[abc]4[ab]c

Would be output as

abcabcabcababababc

Other rules
Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

Characters allowed as input include digits, small English letters and brackets [ ].

Digits are only to represent amount of repetitions.

Letters are just letters.

Brackets are only part of syntax of writing repeated substring.

Input is always valid, so no need to check its validity.
"""

def decom(cstr):
    new_str = ''
    for i, c in enumerate(cstr):
        if c = ']':
            k = 0
            while True:
                word = ''
                num = ''
                start = False
                if start is True and not end_line:
                    num = letter[i-k:n]
                if letter[i-k] == ']':
                    word = letter[i-k:i]
                if letter.isdigit():
                    start = True
                    n = i -k





