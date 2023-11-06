from collections import Counter
import heapq


def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    counts = Counter(hand)
    nums = list(counts.keys())
    heapq.heapify(nums)
    while len(nums) > 0:
        while len(nums) > 0 and counts[nums[0]] <= 0:
            heapq.heappop(nums)
        if len(nums) == 0:
            break
        start = nums[0]
        for n in range(start, start + groupSize):
            if n not in counts or counts[n] <= 0:
                return False
            counts[n] -= 1

    return True



print(isNStraightHand([8,8,9,7,7,7,6,7,10,6], 2))