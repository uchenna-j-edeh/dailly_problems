"""
Problem Statement
Implement a function, findProduct(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

Input:
A list of numbers (can even be floats, integers, and negative!)

Output:
A list such that each index has a product of all the numbers in the list except the number stored at that index.

Sample Input
arr = [1,2,3,4]
Sample Output
arr = [24,12,8,6]
"""

def findProduct(lst):
    product = 1
    for val in lst:
        product *= val

    print(product)    
    for i, val in enumerate(lst):
        lst[i] = product / val

    return lst

print(findProduct([1,2,3,4]))
