# Dynamic programming

test = "00110"
def minFlipsMonoIncr(s):
    res = 0
    currLen = 0
    for c in s:
        if c == "0":
            res = min(currLen, res + 1)
        else:
            currLen += 1
    return res

print(minFlipsMonoIncr(test))