"""
Author: Uchenna Edeh
How do you find the duplicate number on a given integer array?
Algo:
sort the array in O(NlogN). inspect surronding elements for dupplicate om O{N)
"""
def solution1(my_list):
    duplicates = set()
    prev_num = None
    for i in my_list:
        if prev_num is None:
            prev_num = i
            continue

        if prev_num == i:
            duplicates.add(i)
            
        prev_num = i

    return duplicates

list1 = [1, 1, 2, 2, 3, 4, 5]
print(solution1(sorted(list1)))

list2 = [1, 1, 1, 1, 1, 1, 1]
print(solution1(sorted(list2)))

list3 = [1, 2, 3, 4, 5, 6, 7]
print(solution1(sorted(list3)))

list4 = [1, 2, 1, 1, 1, 1, 1]
print(solution1(sorted(list4)))


