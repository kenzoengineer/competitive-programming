# Two Pointer
test = [-10000,-9999,-7,-5,0,0,10000]
def sortedSquares(nums):
    res = []
    p1 = 0
    p2 = len(nums) - 1
    while p1 < p2:
        if abs(nums[p1]) < abs(nums[p2]):
            res.insert(0,nums[p2] * nums[p2])
            p2 -= 1
        else:
            res.insert(0,nums[p1] * nums[p1])
            p1 += 1
    res.insert(0,nums[p1] * nums[p1])
    return res

print(sortedSquares(test))