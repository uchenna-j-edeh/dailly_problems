"""
Given three sorted arrays. Merge them. Duplicates are allowed. Array is already sorted decreasing or increasing. Return them as sorted
"""

def reverse_arr(arr):
    j = len(arr) -1
    for i in range(len(arr)):
        if i == j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        j = j - 1
    return arr

def merge_arrs_helper(a1, a2):
    i = 0
    j = 0

    result = []
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            result.append(a1[i])
            i = i + 1
        elif a2[j] < a1[i]:
            result.append(a2[j])
            j = j + 1
        else:
            result.append(a1[i])
            result.append(a2[j])
            i = i + 1
            j = j + 1

    if i < len(a1):
        result.extend(a1[i:])

    if j < len(a2):
        result.extend(a2[j:])

    return result

def mergeArrays(arr):
    #
    # Write your code here.
    #

    result = []
    is_reversed = False
    for i in arr:
        if len(i) > 1 and i[0] > i[1]:
            i = reverse_arr(i)
            is_reversed = True

        result = merge_arrs_helper(result, i)

    if is_reversed:
        result = reverse_arr(result)

    return result


a = [2, 4, 8, 17]
b = [1, 3, 4, 9]
c = [15, 35, 45, 92]

print(mergeArrays([a, b, c]))

a = [7,3,2]
b = [2,1,0]
c = [1,0,0]

print(mergeArrays([a, b, c]))

