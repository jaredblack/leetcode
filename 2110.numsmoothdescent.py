# fairly straightforward dp
# topic exam problem 1 complete
def getDescentPeriods(prices: list[int]) -> int:
    current_streak = 0
    periods = [0]
    for i, price in enumerate(prices):
        if i > 0 and prices[i-1] == prices[i] + 1:
            current_streak += 1
        else:
            current_streak = 1
        periods.append(periods[-1] + current_streak)
    return periods[-1]


print(getDescentPeriods([3,2,1,4]))