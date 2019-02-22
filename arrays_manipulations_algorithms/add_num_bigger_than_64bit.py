"""
Add numbers bigger than 64 bit number in python...
Example: 9223372036854775807 + 9223372036854775807
"""

def add_outsize_ints(a, b):
    A = [int(num) for num in a]
    B = [int(num) for num in b]

    longer = A
    shorter = B
    len_a = len(A)
    len_b = len(B)

    len_diff = len_a - len_b
    print(A, B)
    if len(B) > len(A):
        longer = B
        shorter = A
        len_diff = len_b - len_a

    len_a = len(A)
    len_b = len(B)
    
    carry_over = 0
    result = []
    print(longer, shorter)
    for i, val in enumerate(longer):
        sum_ab = 0
        idx = len_a - i - 1
        if i + 1 > len_b:
            sum_ab = longer[idx] + carry_over
        else:
            sum_ab = longer[idx] + shorter[idx - len_diff] + carry_over

        sum_ab = sum_ab % 10
        carry_over = sum_ab // 10

        print(sum_ab)     
        result.append(sum_ab)

    return result.reverse()

print(add_outsize_ints('29977', '977'))
#print(add_outsize_ints(9223372036854775807, 9223372036854775807))


    


