
def findFirstUnique(lst):
    my_dict = dict()
    for val in lst:
        if my_dict.get(val, False):
            my_dict[val] += 1
        else:
            my_dict[val] = 1  

    for val in lst:
        if my_dict[val] == 1:
            return val

print(findFirstUnique([9,2,3,2,6,6]))
