# Bit manipulation, dynamic programming

def countBits(n):
    prev = []
    limit = 2
    for i in range(n+1):
        if i <= 1:
            prev.append(i)
            continue
        if i == limit:
            limit *= 2
        prev.append(prev[i-limit]+1)
    return prev