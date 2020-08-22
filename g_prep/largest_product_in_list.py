"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""
def slice_sum(indx, slice_list, ms):
    for i in range(len(slice_list)):
        if i+1 < len(slice_list):
            if ms < slice_list[i] * slice_list[i+1]:
                ms = slice_list[i] * slice_list[i+1]

    
def largest_product(mlist):
    max_sum = 0
    for n in range(len(mlist)):
   #     slice_sum(n, mlist[n:], max_sum) 

       for i in range(n+1, len(mlist)):
           if i+1 < len(mlist):
               if max_sum < mlist[n] * mlist[i] * mlist[i+1]:
                   max_sum = mlist[n] * mlist[i] * mlist[i+1]
    return max_sum

print("The solution is: ", largest_product([-10, -10, 5, 2]))
print("The solution is: ", largest_product([-10, 10, 5, 2]))
