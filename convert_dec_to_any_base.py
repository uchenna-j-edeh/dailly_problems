"""
Author: Uchenna Edeh
converts from base 10 to base n, where n can be any number between 2 and 32
"""

import sys
ALIST=[]
def solution1(num, base):
    #print(num, base)
    global ALIST
    #import pdb; pdb.set_trace()
    div = num // base
    reminder = num % base
    ALIST.append(str(reminder))
    if div == 0:
        return

    solution1(div, base)
    

def main(args):
    if len(args) != 3:
        raise AssertionError("Usage:\n\tpython3 {0} {1} {2}\n\tExpected Result: {3}\n\tPlease Try Again!\n\t".format(__file__, "3", "2", '11' ))
    if int(args[2]) < 2 or int(args[2]) > 32:
        raise ValueError('Select number between 2 and 33 and try again')

    solution1(int(args[1]), int(args[2]))
    result = sorted(ALIST, reverse=True)
    result = ''.join(result)
    print(result)

if __name__ == "__main__":
    try:
        main(sys.argv)
    except(AssertionError, ValueError) as e:
        print(e)
        sys.exit(1)

