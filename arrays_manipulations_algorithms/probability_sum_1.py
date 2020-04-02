"""
You are given n numbers as well as n probabilites that sum up to 1. Write a function
to generate one of the numbers with its corresponding probability. For example, given
the numbers [1, 2, 3, 4] and probabilites [0.1, 0.5, 0.2, 0.2]. Your function should return 1 10% of the time, 2 50% of the time, and 3 and 4
20% od the time.
"""

def calculate(numbers, probabilites):
    for i, v in enumerate(numbers):        
        print("{0} {1}% of the time".format(v, probabilites[i] * 100))

calculate([1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2])