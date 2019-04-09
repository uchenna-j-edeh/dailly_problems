"""
Challenge 10: Rearrange Sorted List in Max/Min Form
Arrange elements in such a way that the maximum element appears at first position, then minimum at second, then second maximum at third and second minimum at fourth and so on.

We'll cover the following
Problem Statement
Input:
Output:
Sample Input
Sample Output
Coding Exercise
Problem Statement
Implement a function called maxMin(lst) which will re-arrange the elements of a sorted list such that the first position will have the largest number, the second will have the smallest, and the third will have second largest, and so on. In other words, all the odd-numbered indices will have the largest numbers in the list in descending order and the even numbered indices will have the smallest numbers in ascending order.

Input:
A sorted list

Output:
A list with elements stored in max/min form

Sample Input
lst = [1,2,3,4,5]
Sample Output
lst = [5,1,4,2,3]
"""

def maxMin(lst):
    i = 0
    len_list = len(lst)
    while(i < len_list):
        #elem = lst[len_list - 1]
       temp = lst.pop()
       lst.insert(i, temp) 
       i = i + 2

    return lst

print(maxMin([1,2,3,4,5]))
       
        
        
