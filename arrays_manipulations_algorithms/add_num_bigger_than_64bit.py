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



    if result[0] == '0':
        result = ['1'] + result
    return ''.join(result)

print(add_outsize_ints('99977', '977'))
print(add_outsize_ints(
    '99999999999999999999999999999999999999999906940404999999999999999999999999999999999999999999999999999999999999999223372036854775807', 
    '999998549548949845984598494985854948954945849589549845785958949458999999999999999999999999999999999999999999999999999999999999999999223372036854775807'))


    


