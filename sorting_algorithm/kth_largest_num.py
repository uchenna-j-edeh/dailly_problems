"""
Extract kth largest word or all list if less than k
return repeated numbers once
"""

import heapq

def topK(arr, k):
    seen = dict()
    alist = []
    for a in arr:
        if not seen.get(a, False):
            heapq.heappush(alist, a)
        #else:
            seen[a] = 1

        if len(alist) > k:
            heapq.heappop(alist)
    
    #if len(alist) < k:
    #    return alist
        
    return alist


print(topK([1, 5, 4, 4, 2], 2))
print(topK([1, 5, 1, 5, 1], 3))
arr = [5,6,1,4,1,8,2,4,1,7,9,3,2,1,2]
print(topK(arr, 20))
