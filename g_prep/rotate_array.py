"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0
"""

class Solution1:
    def __init__(self):
        self.nums = []
        self.size = 0

    def swap(self, m, n):
        #import pdb; pdb.set_trace()
        temp = self.nums[m]
        self.nums[m] = self.nums[n]
        self.nums[n] = temp

    def rotate(self, nums, k):
        self.nums = nums
        self.size = len(nums)
        is_odd = self.size % 2 == 1
        j = k

        if is_odd:
            j = k+1

        for i in range(self.size):
            if is_odd and j >= self.size:
                #import pdb; pdb.set_trace()
                self.swap(i, i+1)
            else:
                self.swap(j, i)

        return self.nums

class Solution:
    def rotate(self, nums, k):
        #n = len(nums) - k
        for i in range(k):
            val = nums.pop()
            nums.insert(0,val)

        return nums



class Solution0:
    def rotate(self, nums, k):
        n = len(nums) - k    
        nums = nums[n:] + nums[0:n]
        print(nums)
        return nums
 

Sol = Solution()
print("The solution is: ", Sol.rotate([-1,-100,3,99], 2))
print("The solution is: ", Sol.rotate([1,2,3,4,5,6,7], 3))
