from functools import cache


def numRollsToTarget(n: int, k: int, target: int) -> int:
    @cache
    def recurse(n, target):
        if n == 0:
            if target == 0:
                return 1
            else:
                return 0
    
        total = 0
        for roll in range(1, k+1):
            total += recurse(n-1, target - roll)
        return total

    return recurse(n, target) % (10**9 + 7)


print(numRollsToTarget(3, 6, 7))
