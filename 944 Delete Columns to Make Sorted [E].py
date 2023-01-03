# String, Array

test = ["abc","bce","cae"]
def minDeletionSize(strs):
    res = 0
    for i in range(len(strs[0])):
        for s in range(1,len(strs)):
            if strs[s-1][i] > strs[s][i]:
                res += 1
                break
    return res
print(minDeletionSize(test))