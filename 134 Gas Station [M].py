# Greedy, Array

g = [1, 2, 3, 4, 5]
c = [3, 4, 5, 1, 2]


def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    current = 0
    index = 0
    for i in range(len(gas)):
        current += gas[i] - cost[i]
        if current < 0:
            current = 0
            index = i + 1
            continue
    return index


print(canCompleteCircuit(g, c))
