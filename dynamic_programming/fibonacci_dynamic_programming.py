from pprint import pprint as pp
# Dynamic Programming

def fibonacci(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#print fibonacci(50)



def mem_fibonacci(n, memo):
    if (n < 0):
        return 0
    if (n <= 1):
        return 1
    if not memo.get(n, False):     
        memo[n] = mem_fibonacci(n - 1, memo) + mem_fibonacci(n - 2, memo)
    return memo[n]

memo = {}
mem_fibonacci(50, memo)
pp(memo)
