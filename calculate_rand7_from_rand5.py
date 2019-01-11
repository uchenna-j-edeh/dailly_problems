"""
Author: Uchenna Edeh
Using a function rand5() that returns an integer from 1 to 5(inclusive) with uniform probability.
Implement a function rand7() that returns an integer from 1 and 7(inclusive).
"""
import random
import sys
from datetime import datetime

def solution1():
    return rand7() 

def rand5():
    """prints a random number between 1 and 5 inclusive"""
    return random.randint(1,5)    

def rand7():
    """prints a random number betwwen 1 and 7 inclusice using rand5 function"""
    A = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    idx = datetime.now().microsecond % 10
    
    return  rand5() + A[idx] 

def main(args):
    if len(args) != 1:
        raise AssertionError("Usage:\n\tpython3 {0} \n\t".format(__file__))
    print(solution1())

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)

