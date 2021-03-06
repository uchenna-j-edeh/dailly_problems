# -*- coding: utf-8 -*-
"""
Author:https://www.geeksforgeeks.org/edit-distance-dp-5/
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.

Algorithms:
What are the subproblems in this case?
The idea is process all characters one by one staring from either from left or right sides of both strings.
Let us traverse from right corner, there are two possibilities for every pair of character being traversed.

m: Length of str1 (first string)
n: Length of str2 (second string)
If last characters of two strings are same, nothing much to do. Ignore last characters and get count for remaining strings. So we recur for lengths m-1 and n-1.
Else (If last characters are not same), we consider all operations on ‘str1’, consider all three operations on last character of first string, recursively compute minimum cost for all three operations and take minimum of three values.
Insert: Recur for m and n-1
Remove: Recur for m-1 and n
Replace: Recur for m-1 and n-1
"""
import sys

def solution1(str1, str2, m , n):
    """A recursion approach grows O(3^m) where m is the length os string"""
    # If first string is empty, the only option is to 
    # insert all characters of second string into first 
    if m==0: 
         return n 
  
    # If second string is empty, the only option is to 
    # remove all characters of first string 
    if n==0: 
        return m 
  
    # If last characters of two strings are same, nothing 
    # much to do. Ignore last characters and get count for 
    # remaining strings. 
    if str1[m-1]==str2[n-1]: 
        return solution1(str1,str2,m-1,n-1) 
  
    # If last characters are not same, consider all three 
    # operations on last character of first string, recursively 
    # compute minimum cost for all three operations and take 
    # minimum of three values. 
    return 1 + min(solution1(str1, str2, m, n-1),    # Insert 
                   solution1(str1, str2, m-1, n),    # Remove 
                   solution1(str1, str2, m-1, n-1)    # Replace 
                   ) 

# A Dynamic Programming based Python program for edit 
# distance problem 
def solution2(str1, str2, m, n): 
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m+1): 
        for j in range(n+1): 
  
            # If first string is empty, only option is to 
            # isnert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n] 


def main(args):
    if len(args) != 3:
        raise AssertionError("Usage:\n\tpython3 {0} {1} {2}\n\tExpected Result: {3}\n\tPlease Try Again!\n\t".format(__file__, "kitten", "sitting", 3 ))
    print(solution2(args[1], args[2], len(args[1]), len(args[2])))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
        sys.exit(1)
