# Two Pointer
test = [2,7,11,15]
t = 9
def twoSum(nums, target):
    s = dict()
    for i in range(len(nums)):
        if target - nums[i] in s:
            return [i,s[target-nums[i]]]
        s[nums[i]] = i
print(twoSum(test,t))