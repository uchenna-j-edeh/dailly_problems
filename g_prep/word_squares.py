"""
https://techdevguide.withgoogle.com/resources/former-coding-interview-question-word-squares/#code-challenge

A 'word square' is an ordered sequence of K different words of length K that, when written one word per line,
reads the same horizontally and vertically. For example:
BALL
AREA
LEAD
LADY

Efficeint solution:
Running a backtracking algorithm with a trie T and an array P of k pointers.

At any given point, we have filled in r rows and columns ( per the problem's constraint). And this point, we are left with a (k - r) sized square to fill. We could use the last (k - r) pointers in P to explore the trie.

Say now that the running time of the algorithm is T(N, k), where N is the number of words given in the input. We could write

T(N, k) = N * (T(N - 1, k - 1) + k), because for each word that we try out, we will have to adjust the k pointers, and there are N words in total. Once we have put in the first word, we are left with N - 1 words and a square of size (k - 1) to fill.

Also, T(p, 1) = p * k^2, because if we are left with a square of size 1, and have p potential characters to fill there, we would fill them in one by one, and print out the entire word square. This will be where our recursion terminates.
"""

#!/usr/bin/env python
import collections
import sys
def find_word_squares(words):
    # Preprocess words: O(#words * word-length) time and space
    words_by_letter_position = collections.defaultdict(set)
    for word in words:
        for index, letter in enumerate(word):
            words_by_letter_position[(index,letter)].add(word)
    # For each word, see if we can make a square.  O(#words * word-length^2/2)
    # for speed, assuming that set intersection is ~O(1) for small sets.
    # Worst-case storage is O(#words * word-length) for very very contrived
    # 'words'.  Normal English words will result in much smaller storage demand;
    # there is a practical maximum of ~170,000 English words.
    for word in words:
        # Initialize a set of incomplete possible squares; each item is an N-tuple
        # of words that are valid but incomplete word squares.  We could also do
        # depth-first via recursion/generators, but this approach is a little
        # simpler to read top-to-bottom.
        possible_squares = set([(word,)])
    # As long as we have any incomplete squares:
    while possible_squares:
        square = possible_squares.pop()
        # When matching an incomplete square with N words already present,
        # we need to match any prospective words to the tuples formed by
        # (N, Nth character in word 0), (N, Nth character in word 1), ...
        # Only words which satisfy all of those restrictions can be added.
        keys = [(i, square[i][len(square)]) for i in range(len(square))]
        possible_matches = [words_by_letter_position[key] for key in keys]
        for valid_word in set.intersection(*possible_matches):
            valid_square = square + (valid_word,)
            # Save valid square in 'ret' if it's complete, or save it as
            # a work-to-do item if it's not.
            if len(valid_square) == len(word):
                yield valid_square
            else:
                possible_squares.add(valid_square)
if __name__ == '__main__':
    words = sys.argv[1:]
    print(words)
    for square in find_word_squares(words):
        print(square)




