"""
Given a stream of elements too large to store in memory, pick a random element
from the stream with uniform probability
"""
import random

def scanner(stream, elem):
    i = 0
    while True:
        if stream.next == elem:
            yield i
        i += 1

def simulation(elements):    
    return (i for i in elements)

stream = 1000000

gen = simulation(stream)

num = random(0, stream)

probability = scanner(gen, num)/ len(stream)

print(probability)