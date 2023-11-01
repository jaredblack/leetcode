# Dijkstra can sadly be a little awkward with Python heapq. 
# This is a modified version of Dijkstra that skips a node if we've already visited it with fewer stops along the way.
# Additionally, the big modification is that we push _all_ children onto the priority queue, regardless of how good they
# look. This is to account for the case when there is a solution within k steps, but it isn't found by just looking for the
# best possible solution.
# Anyway, this one was pretty hard. Maybe give this one another look sometime


from collections import defaultdict
import heapq
import math

def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    flight_dict = defaultdict(list)
    for fro, to, price in flights:
        flight_dict[fro].append((to, price))
    steps = [math.inf for _ in range(n)]
    q = [(math.inf, i, 0) for i in range(n)]
    q[src] = (0, src, 0)
    heapq.heapify(q)
    
    while len(q):
        dist, node, stops = heapq.heappop(q)
        if stops <= steps[node] and stops <= k + 1:
            steps[node] = stops
            if node == dst:
                return dist if dist < math.inf else -1
            for to, price in flight_dict[node]:
                alt = price + dist
                heapq.heappush(q, (alt, to, stops + 1))
    return -1
    

print(findCheapestPrice(5, [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]], 0, 4, 1))