import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        # self.nums = [-n for n in nums]
        self.nums = sorted(nums)[-k:]
        heapq.heapify(self.nums)
        self.k = k
        

    def add(self, val: int) -> int:
        if val > self.nums[0]:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]

    # 3 4 5 8
    # 5 8
    # 


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
