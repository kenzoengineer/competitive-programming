# Sliding Window
test = [10,5,2,6]
t_k = 100
def numSubarrayProductLessThanK(nums,k):
    n = 0
    p = 1
    left = 0
    if (k <= 1):
        return 0
    for i in range(len(nums)):
        p *= nums[i]
        while (p >= k):
            p /= nums[left]
            left += 1
        n += i - left + 1
    return n
print(numSubarrayProductLessThanK(test,t_k))