import math

def coinChange(coins: list[int], amount: int) -> int:
    if amount == 0: return 0
    min_coins = [math.inf for _ in range(amount)]
    for i in range(amount):
        for coin in coins:
            if coin-1 <= i:
                base = min_coins[i-coin] if i - coin >= 0 else 0
                min_coins[i] = min(min_coins[i], 1 + base)
    return min_coins[-1] if min_coins[-1] != math.inf else -1
                
print(coinChange([1,2,5], 11))