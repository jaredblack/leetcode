from functools import cache
import math

# using state machine thinking from top online solution
# s0 = no stock
# s1 = have stock
# s2 = cooldown
# the edges between state nodes represent actions such as buy and sell
def maxProfit(prices: list[int]) -> int:
    state = [[0], [-prices[0]], [-math.inf]]
    for price in prices[1:]:
        s0 = max(state[0][-1], state[2][-1])
        s1 = max(state[0][-1] - price, state[1][-1])
        s2 = state[1][-1] + price
        state[0].append(s0)
        state[1].append(s1)
        state[2].append(s2)
    
    return max(state[0][-1], state[2][-1])


print(maxProfit([1,2,3,0,2]))
# naive recursive solution
# very slow. memoization does not do much for me here
def maxProfit2(prices: list[int]) -> int:
    @cache
    def buy(i, money):
        if i >= len(prices):
            return money
        money -= prices[i]
        return max(sell(i+1, money), cool(i+1, money, True))
    
    @cache
    def sell(i, money):
        if i >= len(prices):
            return money
        money += prices[i]
        return cool(i+1, money, False)

    @cache
    def cool(i, money, have_stock):
        if i >= len(prices):
            return money
        return max(cool(i+1, money, have_stock), sell(i+1, money) if have_stock else buy(i+1, money))
    return max(buy(0, 0), cool(0, 0, False))
        
