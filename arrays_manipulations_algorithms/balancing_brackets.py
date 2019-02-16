"""
Author: Uchenna J. Edeh
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""
import sys
import os


def solution1(my_str):
    stack = []
    top_str = ''
    for astr in my_str:
        if top_str == '(' and astr == ')' or top_str == '[' and astr == ']' or top_str == '{' and astr == '}':
            stack.pop()
            if len(stack):
                top_str = stack[-1]
        else:
            stack.append(astr)
            top_str = astr

    return len(stack) == 0

def solution2(my_str):
    """ Extend solution 1 to include characters"""
    stack = []
    top_str = ''
    for astr in my_str:
        if astr not in '[]({})':
            continue
        if top_str == '(' and astr == ')' or top_str == '[' and astr == ']' or top_str == '{' and astr == '}':
            stack.pop()
            if len(stack):
                top_str = stack[-1]
        else:
            stack.append(astr)
            top_str = astr

    return len(stack) == 0
    

def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, "([])[]({})", True ))
    if os.path.exists(args[1]):
        with open(args[1]) as fh:
            lines = fh.readline()
            lines = lines.strip('\r\n')
            #print('printing line =>', lines)
        print(solution1(lines))
    else:
        print(solution1(args[1]))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)

