def runningSum(nums: list[int]) -> list[int]:
    prefix = [nums[0]]
    for num in nums[1:]:
        prefix.append(prefix[-1] + num)
    return prefix