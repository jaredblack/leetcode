import math
# harder version of #53
# these don't need to be separate for loops if I don't want

def maxSubarraySumCircular(nums: list[int]) -> int:
    # normal max
    max_norm = -math.inf
    max_to_here = 0
    for n in nums:
        max_to_here += n
        if max_to_here > max_norm:
            max_norm = max_to_here
        if max_to_here < 0:
            max_to_here = 0

    # wraparound case
    min_sum = math.inf
    sum_so_far = 0
    for n in nums:
        sum_so_far += n
        if sum_so_far < min_sum:
            min_sum = sum_so_far
        if sum_so_far > 0:
            sum_so_far = 0
    tot_sum = sum(nums)
    max_special = tot_sum - min_sum if tot_sum != min_sum else -math.inf
    max_sum = max(max_norm, max_special)
    return max_sum

print(maxSubarraySumCircular([-3,-2,-3]))