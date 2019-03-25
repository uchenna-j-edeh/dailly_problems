"""
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.
For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}
"""

def solution(intervals):
    smallest_interval = intervals[0]
    biggest_interval = intervals[0]

    for interval in intervals:
        if interval[0] < smallest_interval[0]:
            smallest_interval = interval

        if interval[1] > biggest_interval[1]:
            biggest_interval = interval


    return(smallest_interval[1], biggest_interval[0])

intervals = [[0, 3], [2, 6], [3, 4], [6, 9]]
print(solution(intervals))
