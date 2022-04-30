# Sliding Window

str = "abcdedabxyz"

def lengthOfLongestSubstring(s):
    d = dict()
    left = 0
    res = 0
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = i
        else:
            for j in range(left,d[s[i]]):
                del d [s[j]]
            left = d[s[i]] + 1
            d[s[i]] = i
        res = max(res,i - left + 1)
    return res

print (lengthOfLongestSubstring(str))
