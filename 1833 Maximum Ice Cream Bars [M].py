# Sorting

t_1 = [1, 3, 2, 4, 1]
t_2 = 7
def maxIceCream(costs, coins):
    costs.sort()
    for i in range(len(costs)):
        if costs[i] <= coins:
            coins -= costs[i]
        else:
            return i
    return len(costs)

print(maxIceCream(t_1, t_2))
