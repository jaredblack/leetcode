def buildArray(nums: list[int]) -> list[int]:
    perm = [0] * len(nums)
    for i, n in enumerate(nums):
        perm[i] = nums[n]