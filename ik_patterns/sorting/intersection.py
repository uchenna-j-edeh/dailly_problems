"""intersection of two sorted array using two pinter approach
Example [2,5,7,8,9,11] and [1,3,5,12,13]. Intersetion is 5
    """

def intersect(arr1, arr2):

    i = j = 0
    result = []
    while i < len(arr1) and j < len(arr2): # 5
        if arr1[i] > arr2[j]: # 2 > 1 -> true, 2>3 - False| 5>3 -> true
            j = j + 1 # 3
        elif arr1[i] <  arr2[j]:# -, 2<3 -> True, 
            i = i + 1 # 2
        else: # we found intersection, return index
            result.append(arr1[i])
            i = 1+1
            j = j+1
    return result


print(intersect([2,5,7,8,9,11], [1,3,5,12,13]))
print(intersect([2,4,7,8,9,13], [1,3,5,12,13]))


def merge_two_sorted(arr1, arr2):
    i = j = 0
    result = []
    if arr1[i] > arr2[j]: # 2 > 1 -> true, 2>3 - False| 5>3 -> true
        result.append(arr2[j])
        j = j + 1 # 3
    elif arr1[i] <  arr2[j]:# -, 2<3 -> True, 
            result.append(arr1[i])
            i = i + 1 # 2
    else: # we found intersection, return index
            result.append(arr1[i])
            result.append[arr2[j]]
            i = 1+1
            j = j+1


    while i < len(arr1):
        result.append(arr1[i])

    while j < len(arr2[j]):
        result.append(arr2[j])

    return result


print(merge_two_sorted([2,5,7,8,9,11], [1,3,5,12,13]))
print(merge_two_sorted([2,4,7,8,9,13], [1,3,5,12,13]))