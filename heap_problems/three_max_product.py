"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.
For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
You can assume the list has at least three integers.
"""
import heapq

min_heap = []
min_list = []
max_heap = []
max_list = []
heapq.heapify(min_heap)
heapq.heapify(max_heap)

class Solution:
    def three_max_product(self, alist):
        for num in alist:
            heapq.heappush(min_heap, num)
            
            heapq.heappush(max_heap, -1 * num)

            if len(min_heap) > 3:
                heapq.heappop(min_heap)

            if len(max_heap) > 2:
                heapq.heappop(max_heap)

        
        while len(min_heap):
            min_elem = heapq.heappop(min_heap)
            min_list.append(min_elem)

        while len(max_heap):
            max_elem = heapq.heappop(max_heap)
            max_list.append(max_elem* -1)

        print(max_list)
        print(min_list)

        product_min = min_list[0] * min_list[1]
        product_max = max_list[0] * max_list[1]

        if product_max > product_min:
            return product_max * min_list[2]
        else:
            return product_min * min_list[2]

mlist = [-10, -10, 5, 2]
sol = Solution()
print(sol.three_max_product(mlist))

