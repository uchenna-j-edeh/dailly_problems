"""
Assume you have a method isSubstring which checks if one word is a 
substring of another Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using 
only one call to isSubstring (i e , “waterbottle” is a rotation of “erbottlewat”)
"""

def is_rotation(si, s2):
    if len(s1) == len(s2) and s2 in si+si:
        return True
    return False

print(is_rotation("waterbottle", "erbottlewat"))



