# using list as stack
"""
Author: Uchenna Edeh
This work is copyright protected...
translate '3[abc]4[ab]c' into abcabcabcabababc
"""
import sys

final_str = ''

def decompress(args):
    _digits = ''
    _characters = ''
    start_bracket = False 
    original_str = ''
    #import pdb; pdb.set_trace()
    for i in args:
        if i.isdigit():
            _digits = _digits + i

        elif i == '[':
            start_bracket = True

        elif i == ']':

            original_str = original_str + _characters*int(_digits)
            _digits = ''
            _characters = ''
            start_bracket = False

        elif start_bracket is True:
            _characters = _characters + i
        
        else:
            original_str = original_str + i

    return original_str


if __name__ == '__main__':
        print(decompress(sys.argv[1]))
