"""
sort array using heapsort
"""
import heapq

class Solution(object):
    def sortArray(self, nums):
       heapq.heapify(nums) 
       result = []
       while len(nums) != 0:
           result.append(heapq.heappop(nums))
       return result

A = [9, 1, 5, 6, 3, 4, 9, 0]
sol = Solution()
print(sol.sortArray(A))
