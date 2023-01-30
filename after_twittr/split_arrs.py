"""Given a list [1,2,3,10,9,8,4,5,7,6]. return half of entire sum
"""

def split_arr(my_list):
    # first find total sum
    # iterate until sum reaches half. Note the index
    # use the index to slice off the half
    total = sum(my_list)
    half = total // 2
    total_so_far = 0
    for i in range(len(my_list)):
        if total_so_far + my_list[i] > half:
            return my_list[0:i]
        total_so_far += my_list[i]
    return my_list


mylist = [1,2,3,10,9,8,4,5,7,6]
print(split_arr(mylist))
print(split_arr([]))
