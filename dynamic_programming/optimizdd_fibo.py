"""
This implementation uses constant space, meaning that the amount of memory used by the algorithm does not depend on the input size. 
It achieves this by only keeping track of the two previous Fibonacci numbers (a and b) and using them to calculate the current number (c) in each iteration of the loop.
"""

def fib_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1

        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
            # print(b)
        return b

n = 10
print(fib(n))
print(fib_r(n))