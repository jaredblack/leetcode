def shuffle(self, nums: list[int], n: int) -> list[int]:
    new = []
    for i in range(n):
        new.append(nums[i])
        new.append(nums[i + n])
    return new