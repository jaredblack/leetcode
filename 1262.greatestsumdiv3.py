# this one is tricky. I leaned very heavily on a user-submitted solution

import math

def maxSumDivThree(nums: list[int]) -> int:
    # here, dp represents the maximum amount for each remainder possibility
    dp = [[0]*3 for _ in range(len(nums)+1)]
    dp[0][1] = -math.inf
    dp[0][2] = -math.inf
    for i in range(1, len(nums)+1):
        rem = nums[i-1] % 3
        offset = 3 - rem
        for j in range(3):
            adj = (j + offset) % 3
            dp[i][j] = max(dp[i-1][j], dp[i-1][adj] + nums[i-1])
    return dp[-1][0]


print(maxSumDivThree([3,6,5,1,8]))