"""
("tar", "art")
"""

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    my_map = dict()
    for i in range(256):
        my_map[i] = 0

    for w in word1:
        if my_map.get(ord(w), False):
            my_map[ord(w)] = my_map[ord(w)] + 1
        else:
            my_map[ord(w)] = 1

    for k in word2:
        if my_map.get(ord(k), False):
            my_map[ord(k)] = my_map[ord(k)] - 1


    for j in my_map:
        if my_map[j] != 0:
            return False

    return True


print(is_anagram('tart', 'trat')) # returns True
print(is_anagram('strat', 'tract'))



