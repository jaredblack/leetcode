# I did this one as DP but it looks like there is a more efficient greedy solution.

import math
def jump(nums: list[int]) -> int:
    min_jumps = [math.inf for _ in range(len(nums))]
    min_jumps[0] = 0
    for i, n in enumerate(nums):
        for j in range(i+1, i+n+1):
            if j >= len(nums):
                break
            min_jumps[j] = min(min_jumps[j], min_jumps[i] + 1)
    return min_jumps[-1]

print(jump([2,3,1,1,4]))