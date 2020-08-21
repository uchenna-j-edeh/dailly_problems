"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
class Solution:
    def intersect(self, nums1, nums2):
        intersection = []
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                intersection.append(nums2[i])
                nums1.remove(nums2[i])
        return intersection


class Solution0:
    def intersect(self, nums1, nums2):
        intersection = []
        shorter_list = nums1
        longer_list = nums2
        if len(longer_list) < len(shorter_list):
            temp = shorter_list
            shorter_list = longer_list
            longer_list = temp

        llist_sorted = sorted(longer_list)
        slist_sorted = sorted(shorter_list)
        len_llist = len(llist_sorted)
        len_slist = len(slist_sorted)

        if len_slist == 0 or len_llist == 0:
            return []

        j = 0
        for i in range(len(llist_sorted)):
            if  slist_sorted[j] == llist_sorted[i]:
                intersection.append(llist_sorted[i])
                j = j + 1
                #if j > len(slist_sorted) - 1:
                #    return intersection
            #import pdb; pdb.set_trace()
            elif llist_sorted[i] > slist_sorted[j]:
                j = j+1

            if j > len(slist_sorted) - 1:
                return intersection

        return intersection

sol = Solution()
print("The solution is :", sol.intersect( [1,2,2,1], [2,2]))
print("The solution is :", sol.intersect( [1,2,2,1], [2]))
print("The solution is :", sol.intersect( [1], []))
print("The solution is :", sol.intersect( [3,1,2], [1,1]))
print("The solution is :", sol.intersect( [4,9,5], [9,4,9,8,4]))



        
