# Prefix Sum, Array, Set
nums = [23,2,6,4,7]
k = 13 
def checkSubarraySum(nums, k):
    sums = set()
    prefixes = [nums[0]]
    for i in range(1,len(nums)):
        prefixes.append(prefixes[i-1] + nums[i])
        if prefixes[-1] % k == 0:
            return True
        multiple = prefixes[-1] % k
        if prefixes[-1] in sums:
            return True
        while multiple <= prefixes[-1]:
            if multiple in sums:
                return True
            multiple += k
        sums.add(prefixes[-2])
    return False

print(checkSubarraySum(nums,k) == False)