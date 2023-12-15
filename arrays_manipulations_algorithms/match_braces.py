"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
    """


def parse_braces(args):
    results = []
    for a in args:
        i = len(results) - 1
        if a == ']':
            if len(a) and results[-1] == '[':
                results.pop(i)
        elif a == ')':
            if len(a) and results[-1] == '(':
                results.pop(i)
        elif a == '}':
            if len(a) and results[-1] == '{':
                results.pop(i)
        else:
            results.append(a)
    print(results)
    if len(results) == 0:
        return True

    return False
            

print(parse_braces("([])[]({})"))
print(parse_braces("((()"))