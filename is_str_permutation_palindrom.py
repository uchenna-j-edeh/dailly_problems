"""
Author: Uchenna J Edeh
Given a string, check if it is a permutation of a plalindrom
Algo:
to be permutation of a plindrom, we must have no more than one charater that is odd
"""

def solution1(my_str):
    """ flipping a light swithc """
    bits = [0 for i in range(25)] # flood with zeros
    my_str = my_str.lower() 

    for i in my_str: 
        if not i.isalpha():
            continue

        idx = ord(i) - ord('a')
        if bits[idx]: # toggle bits
            bits[idx] = 0
        else:
            bits[idx] = 1

    count = 0
    print(bits)
    for i in bits:
        if i:
            count = 1 + count

        if count > 1:
            return False 
    return True

#my_str = 'Tact Coa'
#my_str = 'tactcoapapa'
my_str = 'qwertyuioplkjhgfdsazxcvbnmmnbvcxzasdfghjklpoiuytrewq'


print(solution1(my_str))
#print(solution1('uchenna'))    
