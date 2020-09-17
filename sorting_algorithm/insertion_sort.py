"""
insertion sort
"""
def swap(A, B):
    temp = A
    A = B
    B = temp

def insertion_sort_td(A, n):
    if n <= 1:
        return
    insertion_sort_td(A, n-1)
    j = n - 1
    while j >= 1:
        if A[j] < A[j-1]:
            #swap(A[j-1], A[j])

            temp = A[j-1]
            A[j-1] = A[j]
            A[j] = temp

        j = j - 1
    return A

A = [9,1,5,6,3,4,9,0]
print(insertion_sort_td(A, len(A)))

def insertion_sort_td_v2(A, n):
    if n <= 1:
        return
    insertion_sort_td_v2(A, n-1)
    nth = A[n-1]
    j = n - 1
    while j >= 1:
        if A[j] < nth:
            #swap(A[j-1], A[j])
            #temp = A[j-1]
            import pdb; pdb.set_trace()
            print("copying {0} into {1}".format(A[j-1], A[j]))
            A[j-1] = A[j]
            #A[j] = temp
        j = j - 1
        A[j] = nth 
    return A

A = [9,1,5,6,3,4,9,0]
print(insertion_sort_td_v2(A, len(A)))

def insertion_sort_bu(A, n):
    for i in range(2, n):
        j = n - 1
        while j >= 1:
            if A[j] < A[j-1]:
            #swap(A[j-1], A[j])

                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp

            j = j - 1
    return A

A = [9,1,5,6,3,4,9,0]
print(insertion_sort_bu(A, len(A)))
