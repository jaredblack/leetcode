# sorting topic exam 6/5
def maximizeGreatness(nums: list[int]) -> int:
    nums.sort()
    curr_index = 0
    greatness = 0
    for num in nums:
        if num > nums[curr_index]:
            curr_index += 1
            greatness += 1
    return greatness