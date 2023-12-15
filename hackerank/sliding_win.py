"""
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

Example



Lily wants to find segments summing to Ron's birth day,  with a length equalling his birth month, . In this case, there are two segments meeting her criteria:  and .

Function Description

Complete the birthday function in the editor below.

birthday has the following parameter(s):

int s[n]: the numbers on each of the squares of chocolate
int d: Ron's birth day
int m: Ron's birth month
Returns

int: the number of ways the bar can be divided
Input Format

The first line contains an integer , the number of squares in the chocolate bar.
The second line contains  space-separated integers , the numbers on the chocolate squares where .
The third line contains two space-separated integers,  and , Ron's birth day and his birth month.
"""

def birthday(s, d, m):
    # Write your code here
    window = s[0:m]
    win_sum = sum(window)
    num_ways = 0
    
    if win_sum == d:
        num_ways += 1

    for i in range(m, len(s)):
        win_sum = win_sum - s[i-m] + s[i]
            
        if win_sum == d:
            num_ways += 1
        
    return num_ways

# test case 1
# arr = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3 ,3, 4, 2, 1]
# d = 18
# m = 7

# test case 2

arr = [5, 2, 2, 1, 5, 3, 2]
d = 9 
m = 3
print(birthday(arr, d, m))