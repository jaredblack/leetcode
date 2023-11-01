from functools import lru_cache
import math

def minCost(n: int, cuts: list[int]) -> int:
    cuts.sort()
    cuts.insert(0,0)
    cuts.append(n)

    @lru_cache(maxsize=10000)
    def cost(li, ri):
        if ri - li <= 1:
            return 0
        minim = math.inf
        for mi in range(li + 1, ri):
            c = cost(li, mi) + cost(mi, ri) + cuts[ri] - cuts[li]
            if c < minim:
                minim = c
        return minim

    return cost(0, len(cuts)-1)

print(minCost(9, [5,6,1,4,2]))
print(minCost(7, [1,3,4,5]))