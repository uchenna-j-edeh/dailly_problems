"""
https://realpython.com/python-heapq-module/
"""

import heapq

def process_topn(data):
    top_3 = heapq.nsmallest(3, results.splitlines(), key=lambda x: float(x.split()[-1]))
    return top_3

results="""\
ChristaWilli 11.80
Marie-JoTa   10.86
ElaThomp 10.71
TBo  10.83
Shelly-Fraser-Pr 10.86
EnglGard 10.94
Michelle-A   10.92
DaSchipp 10.90
"""
res = process_topn(results)

print("\n".join(res))



"""
print("\n".join(top_3))
ElaThomp 10.71
TBo  10.83
Marie-JoTa   10.86
"""
