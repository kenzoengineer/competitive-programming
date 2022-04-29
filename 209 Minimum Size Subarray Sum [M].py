n = [10,2,3]
t = 6

def minSubArrayLen(target, nums):
    l = len(nums) + 1 if nums[0] < target else 1
    s = nums[0]
    p1 = 0
    for p2 in range(1, len(nums)):
        s += nums[p2]
        while (s >= target):
            l = min(l,p2-p1 + 1)
            s -= nums[p1]
            p1 += 1
    return 0 if l == len(nums) + 1 else l

print(minSubArrayLen(t,n))
