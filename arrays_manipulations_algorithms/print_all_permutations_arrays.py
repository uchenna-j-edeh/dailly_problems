"""
Author: Uchenna Edeh
Given a number in the form of a list of digits, return all possible permutations.
For example, given [1,2,3], return [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
"""


def solution(mylist):
    num_pass = 0
    i = 1
    len_list = len(mylist)
    all_lists = []
    all_lists.append(mylist)
    print(mylist)
    while num_pass < len_list - 1:
        temp = mylist[i]
        if i + 1 > len_list - 1:
            num_pass = 1 + num_pass
            mylist[i] = mylist[0]
            mylist[0] = temp
            i = 0
            print(mylist)
        else:
            mylist[i] = mylist[ i + 1 ]
            mylist[i + 1] = temp
            i = i + 1
            print(mylist)
        all_lists.append(mylist)

    return all_lists

print(solution([1,2,3]))
result1 = solution(['U','C','H','E'])
result2 = solution(['E', 'H', 'C', 'U'])
print(result1 + result2)
        
