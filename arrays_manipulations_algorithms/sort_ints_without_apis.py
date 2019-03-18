"""
Author Uchenna Edeh
Example: A = [10000, 8000, 15000]
Bonus: sort inplace
"""

def my_sort_func(mylist):
    for j, val in enumerate(mylist):
        max_val = val
        idx = j
        for i in range(j+1, len(mylist)):
            if mylist[i] > max_val:
                max_val = mylist[i]
                idx =  i

        temp = mylist[idx]
        mylist[idx] = mylist[j]
        mylist[j] = temp
    return mylist 

def my_sort_func_2(mylist):
    k = 0
    while(len(mylist) - 1 - k > 0):
        max_val = mylist[k]
        idx = k
        for i in range(k+1, len(mylist)):
            if mylist[i] > max_val:
                max_val = mylist[i]
                idx =  i
        temp = mylist[idx]
        mylist[idx] = mylist[k]
        mylist[k] = temp
        k = k + 1
        
    return mylist
 
print(my_sort_func([10000, 8000, 15000]))
print(my_sort_func([10000, 8000, 15000, 20000, 30000, 40000, 900000, 7000, 100000, 50000, 150000]))
print(my_sort_func_2([10000, 8000, 15000, 20000, 30000, 40000, 900000, 7000, 100000, 50000, 150000]))
