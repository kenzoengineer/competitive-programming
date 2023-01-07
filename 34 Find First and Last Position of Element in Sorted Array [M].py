import math
nums = [5, 7, 7, 8, 8, 8, 8, 10]
target = 8


def searchRange(nums, target):
    res = []
    l = 0
    r = len(nums) - 1
    m = 0
    while l < r:
        m = (l + r)//2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    res.append(l)

    l = 0
    r = len(nums) - 1
    m = 0
    while l < r:
        m = math.ceil((l + r)/2)
        if nums[m] > target:
            r = m - 1
        else:
            l = m
    res.append(r)
    return res


print(searchRange(nums, target))
