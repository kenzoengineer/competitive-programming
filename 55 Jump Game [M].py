# Greedy, Dynamic Programming

test = [2, 3, 1, 1, 4]
# Greedy approach
def canJump(nums):
    furthest = 0
    i = 0
    while i <= furthest:
        furthest = max(nums[i] + i, furthest)
        if furthest >= len(nums) - 1:
            return True
        i += 1
    return False

print(canJump(test))
