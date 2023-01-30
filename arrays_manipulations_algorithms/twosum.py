from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            for j in range(i+1,len(nums)):
                if  v + nums[j] == target:
                    return [i, j]

    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()
        for i, v in enumerate(nums):
            my_dict[v] = i + 1

        print(my_dict)
        for k in my_dict: #{2:1, 7:2, 11:3, 15:4} | {3:1, 2:2, 4:3}
            diff = target - k
            if my_dict[diff]: 
                return [my_dict[k] - 1, my_dict[diff] - 1]


solution = Solution()

print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4],6))
print(solution.twoSum([3,3],6))
