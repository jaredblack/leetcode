import math

def maxSubArray(nums: list[int]) -> int:
    max_sub = -math.inf
    max_to_here = 0
    for n in nums:
        max_to_here += n
        if max_to_here > max_sub:
            max_sub = max_to_here
        if max_to_here < 0:
            max_to_here = 0
    return max_sub

print(maxSubArray([-5]))