"""
Author: Uchenna Edeh
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[
    ['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']
]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
"""
def is_match(two_d_matrix, word):
   # print("printing rows")
    for rows in two_d_matrix:
        if ''.join(rows) == word:
            print('A RIGHT  Match word found')
            return True

   # print("printing columns")
    counter = 0
    for i,_ in enumerate(two_d_matrix):
        form_word = ''
        for j in range(len(two_d_matrix)):
            form_word = form_word + two_d_matrix[j][i]

        if form_word == word:
            print('A DOWN Match word found')
            return True
        #counter = counter + 1

    print('No match found!')
    return False


two_d_matrix = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']
]

word = input('Enter a word: ')
print(is_match(two_d_matrix, word))
