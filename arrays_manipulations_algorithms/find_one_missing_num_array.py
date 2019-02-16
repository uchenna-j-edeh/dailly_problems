"""
Author: Uchenna Edeh
find missing elements in an area of 100 integers
Algo:
n(n+1)/2
"""


def solution1(series):
    """ sum series and cpmpute..."""
    result = None
    if series:
        result = sum(series)

    length = 1 + len(series)

    total_sum = 0.5 * length * (length + 1)

    missing_num = total_sum - result

    return missing_num


series = [i+1 for i in range(100)]

# remove one num

#print(series)
print(solution1(series[:-1]))
