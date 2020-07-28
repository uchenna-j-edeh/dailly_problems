"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""

def solve(my_str):
    checker = []
    for i in range(26):
        checker.append(0)

    base = ord('a')
    for ms in my_str:
        indx = ord(ms.lower()) - base
        if checker[indx]:
            return False

        checker[indx] = 1
    return True

print('Solution is:', solve('uchenna'))
print('Solution is:', solve('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))


