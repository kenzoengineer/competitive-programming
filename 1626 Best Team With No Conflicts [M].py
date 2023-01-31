# Dynamic Programming, Sorting, Array

def bestTeamScore(scores, ages):
    pairs = []
    for i in range(len(scores)):
        pairs.append([ages[i],scores[i]])
    pairs = sorted(pairs, key=lambda x: x[1])
    pairs = sorted(pairs, key=lambda x: x[0])
    print(pairs)
    dp = list(map(lambda x: x[1], pairs))
    print(dp)
    res = max(dp)
    for i in range(len(pairs)):
        for j in range(i - 1, -1, -1):
            if pairs[i][1] >= pairs[j][1]:
                dp[i] = max(dp[i], pairs[i][1] + dp[j])
        res = max(res, dp[i])
    return res

print(bestTeamScore([1,2,3,5],[8,9,10,1]))