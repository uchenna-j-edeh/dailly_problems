"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
    """

def sub_max_array(nums, k):
    current_sum = sum(nums[0:k]) # 1, 12, -5, -6
    total_so_far = current_sum # 3
    
    for i in range(k, len(nums)):
        current_sum = current_sum + nums[i] - nums[i-k] # 2 + 50 - 1 = 51| 51 + 3 -12 =42
        if current_sum > total_so_far: # 51 > 3
            total_so_far = current_sum # 51
            print(total_so_far)

    return total_so_far / k # 51/4



nums = [1,12,-5,-6,50,3]
k = 4
print(sub_max_array(nums, k))