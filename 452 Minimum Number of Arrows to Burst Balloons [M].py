# Array, Greedy, Sorting

test = [[10, 16], [2, 8], [1, 6], [7, 12]]
def findMinArrowShots(points):
    res = 1
    points.sort(key=lambda x: x[0])
    end = 2**31 - 1
    for point in points:
        if point[0] > end:
            res += 1
            end = point[1]
        else:
            end = min(end, point[1])
    return res

print(findMinArrowShots(test))
