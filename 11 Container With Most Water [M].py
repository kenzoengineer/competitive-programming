# Two Pointer, Array, Greedy

test = [1, 8, 6, 2, 5, 4, 8, 3, 7]
def maxArea(height):
    p1 = 0
    p2 = len(height) - 1
    res = 0
    while p1 != p2:
        res = max(res, (p2 - p1) * min(height[p1], height[p2]))
        if height[p1] < height[p2]:
            p1 += 1
        else:
            p2 -= 1
    return res

print(maxArea(test))
