"""
Problem Statement
Implement a function rightRotate(lst,n) which will rotate the given list by n. This means that the right-most elements will appear at the left-most position in the list and so on. You only have to rotate by one element from the right though.

Input
A list and a number by which to rotate that list

Output:
The given list rotated by n elements

Sample Input
lst = [1,2,3,4,5]
n = 3
Sample Output
lst = [3,4,5,1,2]
"""

def rightRotate(lst, n):
    """ solution with contant space """
    found = False
    i = 0
    while(i < len(lst)):
        if n == lst[i]:
            found = True
            return lst
        temp = lst[i]
        del lst[i]
        lst.append(temp)
        i = i + 1
    
    if found is False:
        return 

def rightRotate2(lst, n):
    """ solution with contant time """
    return lst[n-1:] + lst[:n-1]

print(rightRotate([1,2,3,4,5], 3))
print(rightRotate2([1,2,3,4,5], 3))

