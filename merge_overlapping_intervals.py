"""
Given a list of possible overlapping intervals, return a new list of intervals where all overlapping intervals have been merged
The input list is not necessarily ordered in any way.
for example, given [(1,3), (5,8), (4, 10), (20, 25)], you should return [(1,3), (4, 10), (20, 25)]
"""

def merge_intervals(my_list):
    end = len(my_list)
    seenit = {}
    for i, interval in my_list:
        for j in range(i+1, end):
            is_overlap(my_list[i], my_list[j])

def is_overlapped(val1, val2):
    # first val starts before 
    pass
                
                
my_list = [(1,3), (5,8), (4, 10), (20, 25)]
print merge_intervals(my_list)
