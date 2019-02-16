"""
Author: Uchenna Edeh

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""
import sys

def solution1(my_str):
    unique_counter = 0
    unique_char = ''
    previous_str = ''
    running_str = ''
    #import pdb; pdb.set_trace()

    for i, val in enumerate(my_str):
        if i == 0:
            unique_counter = 1 
            previous_str = val
            #running_str = 
            continue

        if val == previous_str:
            unique_counter = unique_counter + 1
        else:
           running_str = running_str + str(unique_counter) + previous_str 
           unique_counter = 1
           #unique_char = val

        previous_str = val 

    running_str = running_str + str(unique_counter) + previous_str

    return running_str



def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, "AAAABBBCCDAA", "4A3B2C1D2A" ))
    print(solution1(args[1]))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)

