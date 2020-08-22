def solve(my_set, index=0):
    all_sub_sets = []
    set_sum = sum(my_set)
    if len(my_set) == index:
        all_sub_set.append(0) 
    if set_sum == curr_sum:
        return my_sets
    elif set_sum > curr_sum:
        all_sub_sets = solve(my_set, index + 1)
        item = my_set[index]
        more_sub_set = []
        for i in all_sub_sets:
            new_sub_set = []
            new_sub_set.extend(i) # add all the elements i had b4
            new_sub_set.append(item) # for each element i had before, i need to add new element 
            more_sub_set.append(new_sub_set) # take this new list and add it to my new collection. At the end, for this new index, I would have list with all the previous element added to new elemenet
        all_sub_sets.extend(more_sub_set) # new element created for index + 1 gets added to our super set

    return all_sub_sets

print("Solution is: ", solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


