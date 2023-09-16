# Dynamic programming, array

def productExceptSelf(nums):
    res = [1] * len(nums)
    for i in range (1,len(nums)):
        res[i] = res[i-1] * nums[i-1]
    r = nums[-1]
    for i in range(len(nums) - 2, -1 ,-1):
        res[i] = res[i] * r
        r *= nums[i]
    return res

print(productExceptSelf([1,2,3,4]) == [24,12,8,6])