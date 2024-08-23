points = [(1, 2), (4, 6), (7, 8), (2, 3)]  # example points

print("Points:", points)

# function

import math


def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


p1 = points[0]
p2 = points[1]

distance = euclideanDistance(p1,p2)

print(distance)
