"""
input: 'uchenna'
returns {'u':1, 'c':1, 'h':1, 'e':, 'n':2, 'a':1}
"""

def solution(my_name):
    hash = dict()
    for i in my_name:
        if hash.get(i, False):
            hash[i] += 1
        else:
            hash[i] = 1

    return hash

print(solution('uchenna edeh'))
print(solution('christina'))
