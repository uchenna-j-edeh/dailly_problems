"""
Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in S whose sum is exactly x.
Examples:

Input: arr[] = {0, -1, 2, -3, 1}
        sum = -2
Output: -3, 1
If we calculate the sum of the output,
1 + (-3) = -2

Input: arr[] = {1, -2, 1, 0, 5}
       sum = 0
Output: -1
No valid pair exists.

Method 1: Sorting and Two-Pointers technique.

Approach: A tricky approach to solve this problem can be to use the two-pointer technique. But for using two pointer technique, the array must be sorted. Once the array is sorted the two pointers can be taken which mark the beginning and end of the array respectively. If the sum is greater than the sum of those two elements, shift the left pointer to increase the value of required sum and if the sum is lesser than the required value, shift the right pointer to decrease the value. Let’s understand this using an example.

Let an array be {1, 4, 45, 6, 10, -8} and sum to find be 16

After sorting the array
A = {-8, 1, 4, 6, 10, 45}




Now, increment ‘l’ when the sum of the pair is less than the required sum and decrement ‘r’ when the sum of the pair is more than the required sum.
This is because when the sum is less than the required sum then to get the number which could increase the sum of pair, start moving from left to right(also sort the array) thus “l++” and vice versa.

Initialize l = 0, r = 5
A[l] + A[r] ( -8 + 45) > 16 => decrement r. Now r = 4
A[l] + A[r] ( -8 + 10) increment l. Now l = 1
A[l] + A[r] ( 1 + 10) increment l. Now l = 2
A[l] + A[r] ( 4 + 10) increment l. Now l = 3
A[l] + A[r] ( 6 + 10) == 16 => Found candidates (return 1)

Algorithm:

hasArrayTwoCandidates (A[], ar_size, sum)
Sort the array in non-decreasing order.
Initialize two index variables to find the candidate
elements in the sorted array.
Initialize first to the leftmost index: l = 0
Initialize second the rightmost index: r = ar_size-1
Loop while l < r.
If (A[l] + A[r] == sum) then return 1
Else if( A[l] + A[r] < sum ) then l++
Else r–
No candidates in whole array – return 0
"""

def solution(arr, pair_sum):
    i = 0
    j = len(arr) - 1

    arr = sorted(arr)
    while True:
        _sum = arr[i] + arr[j]
        print(i, j)
        print(arr)
        if i == j:
            return -1

        if _sum > pair_sum:
            j = j - 1
        elif _sum < pair_sum:
            i = i + 1
        else:
            return (arr[i], arr[j]) 
    
print(solution([1, 4, 45, 6, 10, -8], 16))
print(solution([1, 4, 45, 6, 10, -8], 26))
