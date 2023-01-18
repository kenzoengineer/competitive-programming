# Array, Dynamic programming

test = [1,-2,3,-2]
def maxSubarraySumCircular(nums):
    minAns = nums[0]
    maxAns = nums[0]
    currMax = -3 * 10**4
    currMin = 3 * 10**4
    s = 0
    for n in nums:
        currMax = max(currMax + n, n)
        currMin = min(currMin + n, n)
        maxAns = max(currMax, maxAns)
        minAns = min(currMin, minAns)
        s += n
    return max(maxAns, s - minAns) if maxAns > 0 else maxAns

print(maxSubarraySumCircular(test))