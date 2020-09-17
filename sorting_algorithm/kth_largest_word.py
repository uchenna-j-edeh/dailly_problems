"""
Take a stream of words and figure out the kth largest...
words = ['My', 'Name', 'is', 'Uchenna', 'Edeh', '.', 'So', 'what', 'is', 'yours', '?']
Uchenna = 7
yours   = 5
Edeh    = 4
Name    = 4
what    = 4

"""

import heapq

def kth_largest(words, k=4):
    alist = []
    for w in words:
        heapq.heappush(alist, len(w))
        if len(alist) > k:
            heapq.heappop(alist)

    return alist[0]

words = ['My', 'Nam', 'is', 'Uchenna', 'Edeh', '.', 'So', 'wh', 'is', 'yours', '?']
print(kth_largest(words))
