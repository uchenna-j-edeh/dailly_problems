"""
Author: Uchenna Edeh
Given a string and a set of characters, return the shortest substring containing all the characters in the set.
For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".
If there is no substring containing all the characters in the set, return null.
"""
def solution(mlist, unq_set):
    mhash = dict()
    for us in unq_set:
        mhash[us] = 1

    num_elem_found = 0
    first_index = 0
    second_index = 0
    current_substring = ''
    shortest_substring = mlist

    i = 0
    len_mlist = len(mlist)
    while(i < len_mlist):
        val = mlist[i]
        if mhash.get(val, False):
            if mhash[val] == 'found':
                continue
            else:
                mhash[val] = 'found'
                num_elem_found = num_elem_found + 1
            
            if num_elem_found == 2:
                second_index = i

            if num_elem_found == 1:
                first_index = i

            if num_elem_found == len(unq_set):
                current_substring = mlist[first_index:i + 1]

            if len(current_substring) < (shortest_substring):
                shortest_substring = current_substring
                i = second_index                
                num_elem_found = 0
                # reset hash
                for ky in mhash:
                    mhash[ky] = 1
        i = i + 1
    return shortest_substring
print(solution("figehaeci", "aei"))
