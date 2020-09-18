"""
input => arr1 = [1,3,5], arr2 = [2,7,9,0,0,0]
outout => arr2 = [1,2,3,5,7,9]
Algo: three way partition
"""

def merge_one_2_two(arr1, arr2):
    a1 = len(arr1) - 1
    a2 = len(arr2) - 1 - a1
    i = len(arr2) - 1

    while i >= 0:
        if arr2[a2] > arr1[a1]:
            arr2[a2], arr2[i] = arr2[i], arr2[a2]           
            a2 = a2 - 1
        else:
            arr1[a1], arr2[i] = arr2[i], arr1[a1]    
            a1 = a1 - 1
        i = i - 1

    return arr2, arr1

arr1 = [1,3,5]
arr2 = [2,7,9,0,0,0]

print(merge_one_2_two(arr1, arr2))

