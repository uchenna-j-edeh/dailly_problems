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
    if len(B) > len(A):
        longer = B
        shorter = A
        len_diff = len_b - len_a
        len_a = len(B)
        len_b = len(A)

    carry_over = 0
    result = []
    last_variable = 0

    for i, val in enumerate(longer):
        sum_ab = 0
        idx = len_a - i - 1
        if i + 1 > len_b:
            _sum = longer[idx] + carry_over
        else:
            _sum = longer[idx] + shorter[idx - len_diff] + carry_over
            
        sum_ab = _sum % 10
        carry_over = _sum // 10

        result = [str(sum_ab)] + result
        if i + 1 == len(longer):
            last_variable = _sum // 10
             
    print(carry_over)
    if last_variable:
        result = [str(last_variable)] + result
    return ''.join(result)

print(add_outsize_ints('99999', '99999'))
print(add_outsize_ints(
    '999999999999999999999999999999999999999999069404049999999999999999999999999999999999999999999999999999999999999992233720368547758079999999900000000000', 
    '999998549548949845984598494985854948954945849589549845785958949458999999999999999999999999999999999999999999999999999999999999999999223372036854775807'))


    


