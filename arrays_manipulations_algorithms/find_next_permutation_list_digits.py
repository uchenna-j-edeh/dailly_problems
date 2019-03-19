"""
Author: Uchenna Edeh
Given a number represented by a list of digits, find the next greater permutation of a number,
in terms of lexicographic ordering. If there is not greater permutation possible, return the 
permutation with the lowest value/ordering

For example, the list [1, 2, 3] should return  [1, 3, 2]. The list [1, 3, 2] should return 
[2, 1, 3]. The list [3, 2, 1] should return [1, 2, 3]
"""

# also handle [3, 1, 2]

def solution(mylist):
    is_next_lower = None
    is_next_higher = None
    previous = 0
    
    for i, val in enumerate(mylist):
        if i == 0:
            previous = val
            continue

        if val > previous:
            if is_next_lower:
                #look for the next element bigger than x
                return shift_values(i, mylist)
            is_next_higher = True
            continue

        if al < previous:
            if is_next_higher:
                return switich_index_or_wraparound(i - 1, i, mylist)
            is_next_lower = True

    
    if not len(mylist):
        return ValueError("No item in the list...")
    elif is_next_higher:
        return shift_values(1, mylist)


    elif is_next_lower:
        return sorted(mylist)

    else: # list contains only the same element throughout
        raise ValueError("List contain the same item")





def shift_values(idx, _list):
    for i in range(idx, len(_list)):
        if _list[i] > _list[idx]:
            return switich_index_or_wraparound(idx, i, _list)
    part1 = _list[:idx]
    part2 = _list[idx:]
    return part2 + part1
    
def switich_index_or_wraparound(a, b, _list):
    
    temp = _list[b]
    _list[b] = _list[a]
    _list[a] = temp

    return _list

print(solution([1, 2, 3]))
