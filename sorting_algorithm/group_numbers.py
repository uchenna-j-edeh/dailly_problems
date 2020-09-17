"""
Group numbers
"""

import heapq

def solve(arr):
    heap_odd = []
    heap_even = []
    
    for elem in arr:
        if elem % 2:
            heapq.heappush(heap_odd, elem)
        else:
            heapq.heappush(heap_even, elem)
    
    result = []
    while len(heap_even) != 0:
        result.append(heapq.heappop(heap_even))
        
    while len(heap_odd) != 0:
        result.append(heapq.heappop(heap_odd))
        
    return result

print(solve([1,2,3,4]))
