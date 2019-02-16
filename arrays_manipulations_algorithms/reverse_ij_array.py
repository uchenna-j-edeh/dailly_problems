# Given a list, write a function "partial_reverse(a, i, j)"
# that will reverse the items in the array a starting at i and ending at j.
# For example, given the array equal to ['A', 'B', 'C', 'D,' 'E', 'F', 'G']:
# a = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# partial_reverse(a, 2, 5)
# result: ['A', 'B', 'F', 'E', 'D', 'C', 'G']

def solution1(a, i, j):
    if not len(a):
        raise ValueError()
        
    
    first_part = a[:i]
    last_part = a[j+1:]
    
    middle_part = a[i:j+1]
    
    result = []
    
    for n in middle_part:
        
        result = [n] + result
        
    return first_part + result + last_part

a = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(solution1(a, 2, 5))
