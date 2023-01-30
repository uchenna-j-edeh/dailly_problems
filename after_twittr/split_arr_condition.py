"""Given an integer array arr[], the task is to check if the input array can be split in two sub-arrays such that: 

Sum of both the sub-arrays is equal.
All the elements which are divisible by 5 should be in the same group.
All the elements which are divisible by 3 (but not divisible by 5) should be in the other group.
Elements which are neither divisible by 5 nor by 3 can be put in any group.
If possible then print Yes else print No.

Examples: 

Input: arr[] = {1, 2} 
Output: No 
The elements cannot be divided in groups such that their sum is equal.


Input: arr[] = {1, 4, 3} 
Output: Yes 
{1, 3} and {4} are the groups satisfying the given condition. 

Given an integer array arr[], the task is to check if the input array can be split in two sub-arrays such that: 

Sum of both the sub-arrays is equal.
All the elements which are divisible by 5 should be in the same group.
All the elements which are divisible by 3 (but not divisible by 5) should be in the other group.
Elements which are neither divisible by 5 nor by 3 can be put in any group.
If possible then print Yes else print No.

Examples: 

Input: arr[] = {1, 2} 
Output: No 
The elements cannot be divided in groups such that their sum is equal.


Input: arr[] = {1, 4, 3} 
Output: Yes 
{1, 3} and {4} are the groups satisfying the given condition. 
"""
def helper(arr, n, start, lsum, rsum):
    if start == n: # 0 == 3|false.
        return lsum == rsum

    if arr[start] % 5 == 0: # 1 % 5 == 0| False
        rsum += arr[start]

    elif arr[start] % 3 == 0: # 1 % 3 == 0| false
        lsum += arr[start]

    else: # (arr, 3, 1, 0+1, 0  ) or (arr, 3, 1, 0, 0+1)
        return helper(arr, n, start+1, lsum + arr[start], rsum) or helper(arr, n, start+1, lsum, rsum + arr[start])

    return helper(arr, n, start + 1, lsum, rsum)

def split_array(arr, n):
    return helper(arr, n, 0, 0, 0) # array, len, start, lsum, rsum
# driver code:

if __name__ == "__main__":
    arr = [1,4,3]
    n = len(arr)

    if (split_array(arr, n)):
        print("Yes")
    else:
        print("No")

# code credited by a user on geekforgeek.org