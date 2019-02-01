"""
Author: Uchenna Edeh
Given two string, find out if one is a permutation of the other
"""

def solution1(my_str1, my_str2):
    if len(my_str1) != len(my_str2):
        return False

    idx = [0 for i in range(127)]

    for i in my_str1:
        if idx[ord(i)]:
            idx[ord(i)] += 1
            continue           
 
        idx[ord(i)] = 1
    
    print(idx)
    print('\n\n')
    for j in my_str2:
        
        idx[ord(j)] -= 1
        if idx[ord(j)] < 0:
            return False
    print(idx) 
    return True

#my_str1 = 'UCHENNA'
#my_str2 = 'NUCHEAN'
my_str1 = '1234567890-=qwertyuiopasdfghjklzxcvbnm'
my_str2 = 'mnbvcxzasdfghjklpoiuytrewq1234567890-='

print(solution1(my_str1, my_str2))
        
        
        
        
