"""
Author: Uchenna Edeh
Implement a job scheduler which takes in a function and an integer and call f after n milliseconds
"""
import sys
import time

def scheduler(callback_a, n):
    # generate time in mill seconds
    my_time = float(n / 1000) 
    time.sleep(my_time)
    # call function 
    callback_a(my_time)
    
    sys.exit(0)

def greetings(elapse):
    print("calling me after {} milliseconds".format(elapse))

def main(args):
    if len(args) != 2:
        raise AssertionError("Usage:\n\t{0} {1} {2}\n\t".format('python3', __file__, '3000'))
    print(scheduler(greetings, int(args[1])))
    #print(solution2([int(x) for x in args[1].split(',')]))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)
