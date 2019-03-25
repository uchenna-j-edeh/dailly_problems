"""
input: 'uchenna'
returns {'u':1, 'c':1, 'h':1, 'e':, 'n':2, 'a':1}
"""

def solution(my_name):
    my_hash = dict()
    for i in my_name:
        if my_hash.get(i, False):
            my_hash[i] += 1
        else:
            my_hash[i] = 1

    return my_hash

print(solution('uchenna edeh'))
print(solution('christina'))
