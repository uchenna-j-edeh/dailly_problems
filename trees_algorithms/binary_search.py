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
print(binary_search(arr, 72))

mylist = [5,6,7,8,9,10,1,2,3]
#def bs_find_max_rotated_arr(arr, i):
def find_pivot(arr): # an element where the one next to it is smaller
    middle = len(arr) // 2 # 9//2 = 4

    if middle == 0: # false
        return -1
    # import pdb; pdb.set_trace()
    if middle + 1 < len(arr) and arr[middle + 1] < arr[middle]: # false
        return middle+1
        
    
    find_pivot(arr[:middle]) # [5,6,7,8] | 
    find_pivot(arr[middle:]) # [9,10,1,2,3]
        

# arr = [5,6,7,8,9,10,1,2,3]
# print(find_pivot(arr))
#print(bs_find_max_rotated_arr(arr, 9))

arr = [5,6,7,8,9,10,1,2,3]

def binary_search2(middle, x):
    #middle = len(arr) // 2

    if middle == 0 or len(arr) - 1:
        return -1

    if x == arr[middle]:
        return x, middle
    elif x > arr[middle]:
        return binary_search(middle, x)
    else:
        return binary_search(middle, x)

arr = '2,5,8,12,16,23,38,56,72,91'
arr = [int(x) for x in arr.split(',')]
print(binary_search2(arr, 4, 72))

mylist = [5,6,7,8,9,10,1,2,3]