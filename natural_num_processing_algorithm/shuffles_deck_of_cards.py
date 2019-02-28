"""
Given a function that generates perfectly random numbers between 1 and k (inclusive), 
where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.
"""
import random
import sys

#cards = [i + 1 for i in range(52)]

def shuffle(k):
    cards = [i + 1 for i in range(k)]
    """ shuffles a deck of 52 cards 100 times """
    # lets shuffle 100 times
    print(cards)
    for i in range(100):
        pos1 = random_generator(k) - 1 # shift result by 1, index must be 0 to 51
        pos2 = random_generator(k) - 1 # shift result by 1, index must be 0 to 51
#        print pos1, pos2

        temp = cards[pos1]
        cards[pos1] = cards[pos2]
        cards[pos2] = temp

    return cards

def random_generator(n):
    """prints a random number between 1 and 5 inclusive"""
    if n > 1:
        return random.randint(1,n)
    else:
        raise ValueError("The number used is invalid...")

print(shuffle(52))
