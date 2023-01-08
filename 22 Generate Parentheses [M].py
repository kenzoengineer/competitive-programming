# Backtracking, Array

test = 3
def generateParentheses(n):
    ans = []
    def bt(res, open, close):
        # if we can't add anymore, return
        if close == 0 and open == 0:
            ans.append(res)
            return
        # if we can still add open, add them
        if open > 0:
            res += "("
            bt(res, open - 1, close)
            res = res[:-1]
        # close if we have enough opens
        if close > open:
            res += ")"
            bt(res, open, close - 1)
            res = res[:-1]
    bt("", n, n)
    return ans

print(generateParentheses(test))
