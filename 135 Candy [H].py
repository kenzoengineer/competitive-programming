# Array, Greedy

def candy(ratings):
    # 2 pass, do left then right
    candy = [1 for _ in range(len(ratings))]
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            candy[i] = candy[i-1]+1
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candy[i] = max(candy[i], candy[i + 1] + 1)
    return sum(candy)

print(candy([3,1,2]) == 5)