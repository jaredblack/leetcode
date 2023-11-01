def rob(nums: list[int]) -> int:
    max_haul = [nums[0]]
    for i in range(1, len(nums)):
        len_opts = min(len(max_haul), 3)
        opts = max_haul[i - len_opts:i]
        opts[-1] -= nums[i]
        max_haul.append(max(max(opts) + nums[i], nums[i]))

    return max_haul[-1]

print(rob([1,2,3,1]))