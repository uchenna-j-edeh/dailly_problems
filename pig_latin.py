"""
Author: Uchenna Edeh
Given a sentence convert the sentence to the modified pig-latin language:

Words beginning with a vowel, remove the vowel letter and append the letter to the end.
All words append the letters 'ni' to the end.
All words incrementally append the letter 'j'. i.e. 'j','jj','jjj', etc..
"""
def solution1(text):

    vowels = ['a', 'e', 'i', 'o', 'u']

    begin_char = None
    end_char = None 

    words = []
    word = ''

    for i in text:
        if i == '':
            if begin_char:
                continue

            begin_char = i
            words.append(word)
            word = ''

        if begin_char and i == '': # end of line
            if end_char:
                continue

            begin_char = None
            end_char = text[i - i]



    #    if begin_char and end_char is None:
        word = word + i
        print(word)

    print(words)

def solution2(text):
    vowels = ['a', 'e', 'i', 'o', 'u']

    words = text.split()
    new_words = []
    print words
    for i, word in enumerate(words):
        new_word = ''
        if word[0] in vowels:
            new_word = word[1:] + word[0]
        else:
            new_word = word

        new_word = new_word + 'ni' + 'j'*(i+1)
        new_words.append(new_word)

    return ' '.join(new_words)


print solution2('The red brown fox jumps over the short fence')
