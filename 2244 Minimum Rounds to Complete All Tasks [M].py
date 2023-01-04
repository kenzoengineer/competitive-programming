# Math, Counting, Greedy, Hash, Array

test = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]

# 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 1 1 2 2 2 3 3 3  4  4  4  5  5  5
# Note that except for the first number edge case, we change every 3 numbers.

def minimumRounds(tasks):
    hash = dict()
    ones = 0
    res = 0
    for task in tasks:
        if task not in hash:
            hash[task] = 1
            ones += 1
        else:
            if hash[task] == 1:
                ones -= 1
            hash[task] += 1
            if hash[task] == 2 or (hash[task] - 1) % 3 == 0:
                res += 1
    if ones > 0:
        return -1
    return res

print(minimumRounds(test))
