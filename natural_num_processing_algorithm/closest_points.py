"""Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)]"""
import math
def distance(p1, p2):
    distance = math.pow((p2[0] - p1[0]), 2) + math.pow((p2[1] - p1[1]), 2) 
    return math.sqrt(distance)

def closest_pt(my_list):
    max_dist = distance(my_list[0], my_list[1] )
    max_points = [my_list[0], my_list[1]]

    for i, v in enumerate(my_list):
        for _, k in enumerate(my_list[i+1:]):
            result = distance(k, v)
            if result > max_dist:
                max_dist = result
                max_points = [k, v]

    return max_points

print(closest_pt([(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3), (6, 6), (-7, 5), (8, 4), (-9, -2)]))


