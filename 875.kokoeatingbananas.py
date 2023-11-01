import math


def minEatingSpeed(piles: list[int], h: int) -> int:
    lo, hi = 1, max(piles)
    res = hi
    while hi >= lo:
        hours = 0
        mid = (lo + hi) // 2
        for pile in piles:
            hours += math.ceil(pile / mid)
        if hours <= h:
            res = min(mid, res)
            hi = mid - 1
        else:
            lo = mid + 1
    return res

print(minEatingSpeed([30,11,23,4,20], 5))