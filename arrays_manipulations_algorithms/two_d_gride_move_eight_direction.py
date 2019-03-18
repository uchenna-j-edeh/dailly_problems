"""
Author: Uchenna Edeh
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""

def solution(input_list):
    #for x, y in input_list:
    steps = 0
    x, y = input_list[0]
    my_list = [
            (x+1, y),
            (x - 1, y),
            (x, y+1),
            (x, y-1),
            (x-1, y-1),
            (x+1,y+1),
            (x-1,y+1),
            (x+1,y-1)
    ]
    print(my_list)
    for i in range(1, len(input_list)):
        print(input_list[i])
        if input_list[i] in my_list:
            steps = steps + 1
        x, y = input_list[i]
        my_list = [
            (x+1, y),
            (x - 1, y),
            (x, y+1),
            (x, y-1),
            (x-1, y-1),
            (x+1,y+1),
            (x-1,y+1),
            (x+1,y-1)
    ]

    return steps

print(solution([(0, 0), (1, 1), (1, 2)]))
print(solution([(0, 0), (1, 1), (1, 2), (1, 3)]))

