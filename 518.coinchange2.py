# the trick here over the below solution is realizing that when adding a coin,
# we can look at how many ways we could get to the amount without one of that coin
# i.e. look "that coin" number of spaces back on our current row, since that will
# capture all the possible number of occurrences of that coin
# this one is hard !! but its solution is generalizable to knapsack, etc
def change(amount: int, coins: list[int]) -> int:
    if amount == 0:
        return 1
    dp = [[0 for _ in range(amount)] for _ in range(len(coins))]
    for j in range(amount):
        if coins[0] <= (j + 1) and (j+1) % coins[0] == 0:
            dp[0][j] = 1
    for i in range(1, len(coins)):
        for j in range(0, amount):
            above = dp[i-1][j] if i > 0 else 0
            ways_with_current_coin = dp[i][j - coins[i]] if j - coins[i] >= 0 else 0
            if j - coins[i] == -1:
                ways_with_current_coin = 1
            dp[i][j] = above + ways_with_current_coin
    return dp[-1][-1]

print(change(7, [1,2,5]))
# this is a semi-dp solution that is just barely fast enough to pass all the test cases
# but involves a good amount of re-computation with the 3rd inner for loop.
# took me a while to come up with this
def change2(amount: int, coins: list[int]) -> int:
    if amount == 0:
        return 1
    dp = [[0 for _ in range(amount)] for _ in range(len(coins))]
    for j in range(amount):
        if coins[0] <= (j + 1) and (j+1) % coins[0] == 0:
            dp[0][j] = 1
    for i in range(1, len(coins)):
        for j in range(0, amount):
            above = dp[i-1][j] if i > 0 else 0
            quo = (j+1) // coins[i]
            ways_with_this_coin = 0
            for k in range(1, quo+1):
                rem = (j+1) - k * coins[i]
                ways_with_this_coin += dp[i-1][rem - 1] if rem > 0 else 1
            dp[i][j] = above + ways_with_this_coin if quo > 0 else above
    return dp[-1][-1]