"""Example: arr1 = [3,4,7,11], arr2 = [0,2,3,34]. Result = [0,2,3,3,4,7,11,34]
"""

def merge_arrs(arr1, arr2):
    m = 0
    n = 0
    result = []
    while (m < len(arr1) and n < len(arr2)):
        if arr1[m] < arr2[n]:
            result.append(arr1[m])
            m = m + 1
        elif arr2[n] < arr1[m]:
            result.append(arr2[n])
            n = n + 1
        else:
            result.append(arr1[m])
            result.append(arr2[n])
            m = m + 1
            n = n + 1

    
    while m < len(arr1):
        result.append(arr1[m])
        m = m + 1

    while n < len(arr2):
        result.append(arr2[n])
        n = n + 1

    return result


print(merge_arrs([3,4,7,11], [0,2,3,34]))

