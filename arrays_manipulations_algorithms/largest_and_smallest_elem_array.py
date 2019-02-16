"""
Author: Uchenna Edeh
How to find largest and smallest number from integer array 
"""
def solution1(my_list):
    inf = float("inf")
    largest_num = -inf
    smallest_num = inf

    if not len(my_list):
        return ValueError('List cannnot be empty') 

    for num in my_list:
        if num > largest_num:
            largest_num = num

        if num < smallest_num:
            smallest_num = num


    return largest_num, smallest_num


print(solution1([-20, 34, 21, -87, 92, 2147483647]))
#Largest number in array is : 2147483647
#Smallest number in array is : -87
#Given integer array : [10, -2147483648, -2]
#Largest number in array is : 10
#Smallest number in array is : -2147483648
#Given integer array : [2147483647, 40, 2147483647]
#Largest number in array is : 2147483647
#Smallest number in array is : 40
#Given integer array : [1, -1, 0]
#Largest number in array is : 1
#Smallest number in array is : -1
