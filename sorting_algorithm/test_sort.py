#
# Complete the 'merge_sort' function below.
#
# The function accepts an integer array as parameter.
#

def merge_sort_helper(A, start, end):
    if start <= end:
        return
    
    mid = (start + end) // 2
    
    merge_sort_helper(A, start, mid)
    merger_sort_helper(A, mid+1, end)
    
    i = start
    j = mid + 1
    
    aux = []
    
    while i <= mid and j <=end:
        if A[i] <= A[j]:
            aux.append(A[i])
            i = i+ 1
        else:
            aux.append(A[j])
            j = j + 1
            
    while i <= mid:
        aux.append(A[i])
        i = i + 1
        
    while j <= end:
        aux.append(A[j])
        j = j + 1
        
    for i in range(len(aux)):
        A[start] = aux[i]
        start = start + 1
    
    return A
    
def merge_sort(arr):
    # Write your code here
    merge_sort_helper(arr, 0, len(arr) - 1)
    
    return arr
arr = [0, 1, 3, 2]
print(merge_sort(arr))

