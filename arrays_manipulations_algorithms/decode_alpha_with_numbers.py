"""
Author: Uchenna Edeh
Example 111 equivalent to aaa, ak, ka where a=1, b=2, c=3,...z=26
"""
from pprint import pprint as pp
import sys
import math

def solution1(number):
    hash = dict()
    a_char = ord('a')
    z_char = ord('z')
    characters = []

    for ch in range(a_char,  z_char + 1):
        characters.append(chr(ch))

    for i, val in enumerate(characters):
        hash[i+1] = val

    len_str = len(number) 
    my_collection = []
    for i in range(len_str):
        if i == 0:
            # special case
            all_char = ''
            for j in list(number):
                try:
                    all_char = all_char + hash[int(j)] 
                except KeyError:
                    raise KeyError('Invalid value {0}.'.format(j))

            my_collection.append(all_char)
            continue

        number = int(number)
        multiplier = math.pow(10, i) 

        division = int (number / multiplier)
        remainder = number % multiplier

        try:
            my_collection.append(hash[division] + hash[remainder])
        except KeyError:
            raise KeyError('Invalid value {0} or {1}.'.format(division, remainder))

    return my_collection

    #pp(hash)

def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\t{0} {1} '{2}'\n\tExpected Result: {3}\n\tPlease Try Again!\n\t".format('python3', __file__, '111', 'aaa, ak, ka' ))
    print(solution1(args[1]))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except (AssertionError, KeyError) as e:
        print(e)
        sys.exit(0)
