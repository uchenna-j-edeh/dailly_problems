"""
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple true pales, pale -> true pale, bale -> true pale, bae -> false
"""
def replace_str(first, second):
    diff_count = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            diff_count = diff_count + 1
        if diff_count > 1:
            return False
    return True

def delete_str(first, second):
    diff_count = 0
    j = 0
    for i in range(len(first)):
        if i+1 > len(second): # edge case
            return True

        if first[i] != second[j]:
            diff_count = diff_count + 1
            j = j - 1
        if diff_count > 1:
            return False

        j = j + 1
    return True

def inser_str(first, second):
    return delete_str(second, first)

def solution(first_str, second_str):
    if len(first_str) == len(second_str):
        return replace_str(first_str, second_str)
    elif len(first_str) == len(second_str) + 1:
        return delete_str(first_str, second_str)
    elif len(first_str) + 1 == len(second_str):
        return insert_str(first_str, second_str)
    else:
        return False

print("The solution is :", solution('pale', 'ple'))
print("The solution is :", solution('pales', 'pale'))
print("The solution is :", solution('pale', 'bale'))
print("The solution is :", solution('pale', 'bae'))
