from collections import Counter, deque
import heapq


def leastInterval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    heap = [-count for count in counts.values()]
    heapq.heapify(heap)
    idle_q = deque()
    time = 0
    while len(heap) > 0 or len(idle_q) > 0:
        if len(idle_q) and idle_q[-1][1] < time:
            heapq.heappush(heap, idle_q.pop()[0])
        if len(heap):
            freq = heapq.heappop(heap)
            if freq < -1:
                idle_q.appendleft((freq + 1, time + n))
        time += 1
    return time
    


print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))