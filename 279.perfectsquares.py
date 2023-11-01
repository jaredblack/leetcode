import math

# DP topic exam problem 3
# pretty much just the same as minimum number of coins. 
# precompute the squares and those are the coins
def numSquares(n: int) -> int:
    squares = [n**2 for n in range(1, int(math.sqrt(n)) + 1)]
    res = []
    for i in range(1, n+1):
        min_new = math.inf
        for sq in squares:
            if sq < i:
                cand = 1 + res[i - sq - 1]
                if cand < min_new:
                    min_new = cand
            elif sq == i:
                min_new = 1
                break
            elif sq > i:
                break
        res.append(min_new)
    return res[-1]

print(numSquares(12))