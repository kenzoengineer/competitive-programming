# Prefix sum, Array

t_1 = [4,5,0,-2,-3,1]
t_2 = 5
def subarraysDivByK(nums, k):
    prefix = [nums[0]]
    res = 0
    for i in range(1,len(nums)):
        prefix.append(prefix[-1] + nums[i])
    for i in range(len(nums)):
        if prefix[i] % k == 0:
            res += 1
            print("a ",nums[0:i+1])
        for j in range(0, i):
            if (prefix[i] - prefix[j]) % k == 0:
                print("b ",nums[j+1:i+1])
                res += 1
    return res
    


print(subarraysDivByK(t_1,t_2))