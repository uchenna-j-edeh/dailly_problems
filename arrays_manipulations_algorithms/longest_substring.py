"""
Author: Uchenna Edeh
Example 'a beautiful day!' would give 'ul day!'
"pwwkew" should produce "wke"
"""
import sys

def solution1(my_str):
    longest_str = ''
    running_total = ''
    hash = dict()
    for _char in my_str:
        if hash.get(_char, False):
            #print(running_total)
            #print(longest_str)
            if len(running_total) > len(longest_str):
                longest_str = running_total
            hash = dict()
            hash[_char] = 1
            running_total = _char

        else:
            running_total = running_total + _char
            hash[_char] = 1

    if len(running_total) > len(longest_str):
        longest_str = running_total

    return (len(longest_str), longest_str)

def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, "a beautiful day!", '(7, ul day!)' ))
    print(solution1(args[1]))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)
