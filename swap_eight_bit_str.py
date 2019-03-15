"""
Author: Uchenna Edeh
Given an unsigned 8-bit integer, swap its even and odd bits.
The 1st and 2nd should be swapped, the 3rd and the 4th should be swaqpped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001
Bonus: Can you do it in one line?
"""

def swap_eight_bits(eb):
    return ''.join([eb[i:i+2][1] + eb[i:i+2][0] for i in range(0, len(eb), 2)])



    #return ''.join([eb[i] + eb[i-1]  for i in range(0, len(eb), 2)])

print(swap_eight_bits('10101010'))
print(swap_eight_bits('11100010'))
