"""
Author Uchenna Edeh
given a list example [10, 4, 3,9, 7]. Figure if given a number k. There two numbers that sums up to k. If k is 7, then 10 + 7 is 17.
"""
import sys

def sum_two_numbers(nlist, k):
    ndict = dict()
    for nl in nlist:
        nl = int(nl)
        #ndict[nl] = 1
        ndiff = int(k) - nl
        if ndict.get(ndiff, False):
            #print('Found the matching numner', nl)
            return ndiff, nl
        ndict[nl] = 1

def main(args):
    if len(args) != 3:
        raise AssertionError("Usage:\n\t{0} {1} '{2}' {3}\n\tExpected Result: {4}\n\tPlease Try Again!\n\t".format('python3', __file__, '10,4,3,9,7', '17', '(10, 7)' ))
    print(sum_two_numbers(args[1].split(','), args[2]))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(0)


