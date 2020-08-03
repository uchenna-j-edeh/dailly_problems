"""
Subset Sum | Backtracking-4
Subset sum problem is to find subset of elements that are selected from a given set whose sum adds up to a given number K. We are considering the set contains non-negative values. It is assumed that the input set is unique (no duplicates are presented).

Exhaustive Search Algorithm for Subset Sum

One way to find subsets that sum to K is to consider all possible subsets. A power set contains all those subsets generated from a given set. The size of such a power set is 2N.

Backtracking Algorithm for Subset Sum

Using exhaustive search we consider all subsets irrespective of whether they satisfy given constraints or not. Backtracking can be used to make a systematic consideration of the elements to be selected.
"""

def create_subset(arr, a):
    arr.remove(a)
    return arr

def solution(arr, arr_sum):
    print(arr)
    if sum(arr) == arr_sum:
        return arr

    for i in arr:
        #print(i, arr)
        new_arr = create_subset(arr[:], i)
        curr_sum = sum(new_arr)
        if curr_sum == arr_sum:
            return new_arr
        elif curr_sum > arr_sum:
            solution(new_arr, arr_sum)

# input most be sorted
#print('The solution is', solution([1, 2, 3, 4, 6, 8, 9, 12, 15, 29], 6))
print('The solution is', solution([8, 9, 12, 15, 29], 56))
#print('The solution is', solution([8, 9, 12, 15, 29], 65))

