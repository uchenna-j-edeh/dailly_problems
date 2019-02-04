"""
Author: Uchenna Edeh
The problem: Given an unsorted array of numbers, find the maximum difference between the successive elements in its sorted form. The numbers can be negative or decimals.
Example: '21,41,17,45,9,28' should return 13
"""

def solution1(my_nums):
    #find max and min
    my_max = my_nums[0] 
    my_min = my_nums[0] 

    for i in my_nums:
        if i > my_max:
            my_max = i
            
        if i < my_min:
            my_min = i

    start_point = 0
    if my_min < 0:
        start_point = my_min

    int_seq = [0 for i in range(my_max+1)]
    print(int_seq)

    
    for k in my_nums:
        int_seq[k] = int_seq[k] + 1

    print(int_seq)
    new_nums = []
    for j, val in enumerate(int_seq):
        if val:
            for n in range(val):
                new_nums.append(j)

    print(new_nums)

nums = '21,41,17,45,9,28'

print(solution1([int(x) for x in nums.split(',')]))

