"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
"""
def delete_dups(mlist):
     i = 0
     len_arr = len(mlist)
     while(i+1 < len_arr):
        if mlist[i] == mlist[i+1]:
            del mlist[i]
            i = i - 1
            len_arr = len_arr - 1

        i = i + 1

     return mlist


print("solution is: ...", delete_dups([1,1,2]))
print("solution is: ...", delete_dups([0,0,1,1,1,2,2,3,3,4]))

