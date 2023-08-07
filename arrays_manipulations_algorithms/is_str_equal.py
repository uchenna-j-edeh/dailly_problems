# write a code to check if two str are equal

def is_equal(s1, s2):

    for i in range(len(s1)):
        # if len(s2) - 1 >= i:
        #     return False
        
        if  len(s2) - 1 >= i or (s1[i].lower() != s2[i].lower()):
            return False
        
    for i in range(len(s2)):
        # if len(s1) - 1 >= i:
        #     return False
        
        if  len(s1) - 1 >= i or (s1[i].lower() != s2[i].lower()): # i = 4, len(s1) = 4
            return False
    return True


s1 = "abcd" # 4
s2 = "ABCDj" # 5

print(is_equal(s1, s2))