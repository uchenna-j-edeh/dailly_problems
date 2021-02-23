"""
solve n! by recursion...
"""
def fn(n):
    if n == 0:
        return 1

    return n * fn(n -1)

print(fn(20))
print(fn(0))
print(fn(10))
print(fn(5))
