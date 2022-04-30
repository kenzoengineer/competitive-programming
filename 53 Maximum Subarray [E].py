# Sliding Window

arr = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums) -> int:
    local_max = nums[0]
    actual_max = nums[0]
    for x in nums[1:]:
        local_max = max(x, local_max + x)
        actual_max = max(actual_max, local_max)
    return actual_max
print(maxSubArray(arr))