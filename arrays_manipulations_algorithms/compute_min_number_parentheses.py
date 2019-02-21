"""
Given a string of parentheses, write a function to compute the minimum number of
parentheses to be removed to make the string valid (i.e each open parentheses is 
eventually closed)

For example, given the string "()())()", you should return 1. Given the string ")(",
you should return 2, since we must remove all of them
"""

def solution(my_str):
    top_char = ''
    stack = []
    
    for i in my_str:
        if top_char == '(' and i == ')':
            stack.pop()
            if len(stack)> 0:
                top_char = stack[-1]
            else:
                top_char = ''
        else:
            stack.append(i)
            top_char = i

    return len(stack)

print(solution("()())()"))
print(solution("(()())()"))
print(solution(")("))
