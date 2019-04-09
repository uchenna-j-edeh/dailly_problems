
def findMinimum(lst):
    if not lst:
        return None

    min_num = lst[0]
    
    for val in lst:
        if val < min_num:
            min_num = val

    return min_num

print(findMinimum([9,2,3,6])) 
