class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self._updatePrefix()
        
    def _updatePrefix(self):
        self.prefix = [self.nums[0]]
        for num in self.nums[1:]:
            self.prefix.append(self.prefix[-1] + num)
        return self.prefix

        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - (self.prefix[left-1] if left > 0 else 0)