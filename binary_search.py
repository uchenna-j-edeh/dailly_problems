"""
find a give number in list of sorted array. If the number is not there, return -1
Example: '2,5,8,12,16,23,38,56,72,91', find 12
"""

def binary_search(arr, x):
    middle = len(arr) // 2

    if middle == 0:
        return -1

    if x == arr[middle]:
        return x, middle
    elif x > arr[middle]:
        return binary_search(arr[middle:], x)
    else:
        return binary_search(arr[:middle], x)

arr = '2,5,8,12,16,23,38,56,72,91'
arr = [int(x) for x in arr.split(',')]
print(binary_search(arr, 8))

arr = [5,6,7,8,9,10,1,2,3]

def bs_find_max_rotated_arr(arr, i):
    j = len(arr) // 2
    if j == 0:
        return -1

    if  arr[j+1] < arr[j]:
        return arr[middle] 
    else: 
       # pick one side, search it
       return bs_find_max_rotated_arr(arr, j)

     
arr = [5,6,7,8,9,10,1,2,3]
print(bs_find_max_rotated_arr(arr, 9))
