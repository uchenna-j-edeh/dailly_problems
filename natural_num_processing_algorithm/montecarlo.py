"""
Author: Uchenna Edeh

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.
Algorithm from wikipedia
For example, consider a quadrant inscribed in a unit square. Given that the ratio of their areas is π / 4, the value of π can be approximated using a Monte Carlo method:[11]

Draw a square, then inscribe a quadrant within it
Uniformly scatter a given number of points over the square
Count the number of points inside the quadrant, i.e. having a distance from the origin of less than 1
The ratio of the inside-count and the total-sample-count is an estimate of the ratio of the two areas, π / 4. Multiply the result by 4 to estimate π.
"""
import random
import math
import sys
from datetime import datetime

def solution1(total_count):
    counter = 0
    for i in range(total_count):
        x = random.random()
        y = random.random()

        r = math.sqrt( x*x + y*y )

        if r <= 1:
            counter += 1 
        
        yield counter

def solution2(total_count):
    counter = 0
    for i in range(total_count):
        x = random.random()
        y = random.random()

        r = math.sqrt( x*x + y*y )

        if r <= 1:
            counter += 1

    return 4 * counter / total_count


def build_generator_function(limit):
    i = 0
    for i in solution1(limit):
        try:
            continue
        except StopIteration:
            print(i)
            return i  


    return 4 * i / limit 


def main(args):
    now = datetime.now()
    if len(args) != 2:
        raise AssertionError("Usage:\n\t{0} {1} {2}\n\t".format('python3', __file__, 30000))
    print(build_generator_function(int(args[1]))) # Using generator
    #print(solution2(int(args[1])))

    delta = datetime.now() - now
    print("Time Elapse: {0}".format(str(delta)))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(0)
        
