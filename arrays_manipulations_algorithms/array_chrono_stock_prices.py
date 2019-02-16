"""
Author: Uchenna Edeh
Given a array of numbers representing the stock prices of a company
in chronological order, write a function that calculates the maximum profit
you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 
5 dollars and sell it at 10 dollars.
Algorithms:
start searching . Locate both the smallest price first.
once the lowest has been located, note the index 

start another search from the lowest index, to locate the highest price. 
"""

import sys

def solution1(alist):
    len_alist = len(alist)

    # special cases
    if len_alist == 0:
        return 0

    lowest_price = alist[0] 
    lowest_idx = 0
    
    for i, _ in enumerate(alist):
        if alist[i] < lowest_price:
            lowest_price = alist[i]
            lowest_idx = i 

    #print(lowest_price, lowest_idx)
    max_price = lowest_price
    for k in range(lowest_idx, len_alist):
        if alist[k] > lowest_price:
            max_price = alist[k]

    #print(max_price)
    return max_price - lowest_price 
    

def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\tpython3 {0} '{1}'\n\tExpected Result: {2}\n\tPlease Try Again!\n\t".format(__file__, "9, 11, 8, 5, 7, 10", '5' ))
    my_list = [int(x) for x in args[1].split(',')]
    print(solution1(my_list))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)
