# Two Pointer
test = [0,0,1,1,1,2,2,3,3,4]
def removeDuplicates(nums):
    dups = 0
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            dups += 1
        else:
            nums[i-dups] = nums[i]
    return len(nums) - dups


print(removeDuplicates(test))