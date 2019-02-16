"""
Author: Uchenna Edeh
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit(or zero edits) away.
Example:
pale, ple -> true
pales, pale - > true
pale, bale -> true
pale, bae -> false
"""

def solution1(first_word, second_word):
    """ using bits flipping """
    idx = [0 for i in range(25)] 
    for i in first_word:
        n = ord(i) - ord('a')  
        idx[n] = idx[n] + 1
        
    for j in second_word:
        n = ord(j) - ord('a')  
        idx[n] = idx[n] - 1

    count = 0
    print(idx)
    for k in idx:
        if abs(k) > 1:
            return False

        if k:
            count = count + 1 

        if count > 1:
            return False

    return True
word1 = 'apple'
word2 = 'ale'

print(solution1(word2, word1))
