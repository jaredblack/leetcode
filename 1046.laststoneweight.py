import heapq


def lastStoneWeight(stones: list[int]) -> int:
    stones = [-stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        x, y = -heapq.heappop(stones), -heapq.heappop(stones)
        if x > y:
            heapq.heappush(stones, -x + y)
    return stones[0] if len(stones) else 0