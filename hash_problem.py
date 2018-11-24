"""
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

if __name__ == "__main__":
    mlist = sys.argv[1].split(',') 
    k = sys.argv[2]
    print(sum_two_numbers(mlist, k))
