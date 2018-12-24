"""
Author: Uchenna Edeh
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
Algorithm:
    calculate how may words , will be need in advance and how many extra spaces there would be
"""

import sys
def solution1(words, k):
    """Assuming that k would be at least bigger than all the words used"""
    print(k)
    print(words)
    accumulation = 0
    new_text = ''

    for i, val in enumerate(words):

        if len(accumulation) + len(val) > k:
            new_text = normalize_text(words[1+i:], k)
        else:
            accumulation = len(accumulation) + len(val) + 1 # one added to count for space character

    return new_text

def normalize_text(words, k):
    len_words = len(''.join(words))
    num_words = len(words)
    remainder = k - len_words 
    num_location =  num_words - 1

    space_count = remainder / num_location

    remainder = remainder % num_location
    ave_space = ' '*space_count

    _text = ave_space.join(words)
    new_text = ''

    for i in enumerate(_text):

        if remainder and i == ave_space:
            remainder = remainder - 1
            new_text = 



     




def main(args):
    if len(args) != 3:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}' {2}\n\tExpected Result: {3}\n\tPlease Try Again!\n\t".format(__file__, "the quick brown fox jumps over the lazy dog",  "16","\nthe  quick brown\nfox  jumps  over\nthe   lazy   dog"))
    print(solution1(args[1].split(), int(args[2])))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)

