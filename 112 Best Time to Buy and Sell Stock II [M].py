test = [7, 1, 5, 3, 6, 4]


def maxProfit(prices):
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] - prices[i] > 0:
            profit += prices[i + 1] - prices[i]
    return profit


print(maxProfit(test))
