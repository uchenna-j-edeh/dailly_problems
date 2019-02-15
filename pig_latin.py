"""
Author: Uchenna Edeh
Given a sentence convert the sentence to the modified pig-latin language:

Words beginning with a vowel, remove the vowel letter and append the letter to the end.
All words append the letters 'ni' to the end.
All words incrementally append the letter 'j'. i.e. 'j','jj','jjj', etc..
"""

def solution2(text):
    vowels = ['a', 'e', 'i', 'o', 'u']

    words = text.split()
    new_words = ''
    print (words)
    for i, word in enumerate(words):
        new_word = ''
        if word[0] in vowels:
            new_word = word[1:] + word[0]
        else:
            new_word = word

        new_word = new_word + 'ni' + 'j'*(i+1)
        new_words = new_words + new_word + " " 

    return new_words.strip()


print (solution2('The red brown fox jumps over the short fence'))
