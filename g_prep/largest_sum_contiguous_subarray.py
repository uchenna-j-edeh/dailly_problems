"""
Taken from: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""

# Python program to find maximum contiguous subarray 
   
# Function to find the maximum contiguous subarray 
from sys import maxsize 
def maxSubArraySum(a,size): 
       
    max_so_far = -maxsize - 1
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far 
   
# Driver function to check the above function  
#a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
a = [-2,1,-3,4,-1,2,1,-5,4]
#print ("Maximum contiguous sum is", maxSubArraySum(a,len(a)) )
   
#This code is contributed by _Devesh Agrawal_ 

from sys import maxsize
class Solution:
    def maxSubArray(self, nums):
        max_so_far = -maxsize - 1
        max_ending_here = 0
        size = len(nums)

        for i in range(0, size):
            max_ending_here = max_ending_here + nums[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0

        return max_so_far

sol = Solution()
print("The solution is: ", sol.maxSubArray( [-2,1,-3,4,-1,2,1,-5,4]))
