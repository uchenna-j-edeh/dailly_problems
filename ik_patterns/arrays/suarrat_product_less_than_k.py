"""
713. Subarray Product Less Than K
Medium
5K
161
company
Amazon
company
Facebook
company
LinkedIn
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
"""

def product_less_than_k(nums, k): #[10,5,2,6], 100
    count = 0
    total_product = 1
    if nums[0] < k:
        count += 1 # 1
        total_product = nums[0] # 10

    left = 0
    
    for i in range(1, len(nums)): # 5,2,6
        total_product = total_product * nums[i]
        while left <= i and total_product >= k:
                total_product = total_product / nums[left]
                left += 1
            
        count += i - left + 1 # 3, 3 + 


    # count += i - left + 1 # 3 +  4 - 1 + 1
    return count


nums = [10,5,2,6]
k = 100

print(product_less_than_k(nums, k))
