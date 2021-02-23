""""
solve fibonacci sequence...
"""

def add_seq(n, a, b):
    if n == 0:
        return a

    #if n == 1:
    #    return b

    return add_seq(n - 1, b, a + b)

first_base_case = 0
second_base_case = 1

print(add_seq(5, first_base_case, second_base_case))
