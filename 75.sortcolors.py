from collections import Counter

# sorting topic exam 3/5
def sortColors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    color_counts = Counter(nums)
    start_i = 0
    for color in range(3):
        for i in range(start_i, start_i + color_counts[color]):
            nums[i] = color
        start_i += color_counts[color]

