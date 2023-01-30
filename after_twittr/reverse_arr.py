"""
reverse array. example input: ['u', 'c', 'h', 'e'], output:  ['e', 'h', 'c',  'u']
"""

def reverse_arr(my_list): # 
    mid_point = len(my_list) // 2 # 2

    for i in range(mid_point): # 0
        end_point = len(my_list) - i  - 1 # 4 - 0 - 1 = 3,
        tmp = my_list[i] # u
        my_list[i] = my_list[end_point] # u = e,
        my_list[end_point] = tmp # e = u

    return my_list


print(reverse_arr( ['u', 'c', 'h', 'e']))
print(reverse_arr( ['u', 'c', 'h', 'e', 'n', 'n', 'a']))
