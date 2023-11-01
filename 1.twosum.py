def twoSum(nums: list[int], target: int) -> list[int]:
    prev_nums = {}
    for i, n in enumerate(nums):
        if target - n in prev_nums:
            return [i, prev_nums[target - n]]
        prev_nums[n] = i