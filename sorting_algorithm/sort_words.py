"""
input=> ["mark zukerbeng", "tim cook", "mark twain"]
output=>["mark2:zukerbeng", "tim:1,cook"]
"""
import heapq

def solve(arr):
    seen_names = dict()
    for a in arr:
        first, last = a.split()
        if seen_names.get(first, False):
            seen_names[first][0] = seen_names[first][0] + 1
            heapq.heappush(seen_names[first][1], last)
        else:
            seen_names[first] = [1, [last]]

        if len(seen_names[first][1]) > 1:
            heapq.heappop(seen_names[first][1])

    return ["{}:{},{}".format(k, v[0], v[1][0]) for k, v in seen_names.items()]

print(solve(["mark zukerbeng", "tim cook", "mark twain"]))
            

      


