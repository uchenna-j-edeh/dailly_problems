"""
write merge sort algo
"""

def merge_sort_helper(A, start, end):
    if start >= end:
        return

    mid = (start + end) // 2

    merge_sort_helper(A, start, mid)
    merge_sort_helper(A, mid + 1, end)

    # when you have divided array down to it's smalles unit and you begin exection, this piece of code below then runs
    i = start
    j = mid + 1

    aux = [] 
    while i <= mid and j <=end:
        if A[i] <= A[j]:
            aux.append(A[i])
            i = i + 1
        else: # A[i] > A[j]
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
def merge_sort(A):
    merge_sort_helper(A, 0, len(A) - 1)

A = [9,1,5,6,3,4,9,0]
result = merge_sort(A)
print(result)
print(A)

# Read the contents of the file into a Python list
NUMLIST_FILENAME = "QuickSort_List.txt"
inFile = open(NUMLIST_FILENAME, 'r')

with inFile as f: numList = [int(integers.strip()) for integers in f.readlines()]
# call functions to count comparisons
#print(merge_sort(numList))
#print(numList)


