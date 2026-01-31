# Binary search

import math


def minEatingSpeed(piles: list[int], h: int) -> int:
    l = 1
    r = max(piles)
    while l < r:
        speed = (l + r) // 2
        s = 0
        for pile in piles:
            s += math.ceil(pile / speed)
        if s > h:
            l = speed + 1
        else:
            r = speed
    return l


print(minEatingSpeed([3, 6, 7, 11], 8))
print(minEatingSpeed([30, 11, 23, 4, 20], 5))
print(minEatingSpeed([30, 11, 23, 4, 20], 6))
