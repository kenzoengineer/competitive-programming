# Dynamic Programming, Array

t_1 = 3
t_2 = 7
# t_1 lists containing t_2 elements
def uniquePaths(m, n):
    dp = [[0 for x in range(n)] for y in range(m)]
    for i in range(n):
        dp[m-1][i] = 1
    for i in range(m - 2, -1, -1):
        for j in range(n - 1, -1, -1):
            if j == n - 1:
                dp[i][j] = 1
                continue
            dp[i][j] = dp[i + 1][j] + dp[i][j+1]
    return dp[0][0]

print(uniquePaths(t_1, t_2))
