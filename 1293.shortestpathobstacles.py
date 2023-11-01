from collections import defaultdict, deque
import math

# pretty simple in concept, run a BFS on the grid where you're also keeping track of the number of
# breaks left. if you run out of breaks, stop. as soon as you get to the end, return the result
# you found lest it get overwritten by something worse
def shortestPath(grid: list[list[int]], k: int) -> int:
    def in_bounds(i, j):
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])
    
    max_obs = {(0,0):k}
    min_dist = defaultdict(lambda: math.inf)
    min_dist[(0,0)] = 0
    if grid == [[0]]:
        return 0
    

    q = deque()
    q.append((0,0,k))
    while len(q) > 0:
        i,j,k = q.popleft()
        for i1, j1 in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            if not in_bounds(i1, j1):
                continue
            k1 = k
            if grid[i1][j1] == 1:
                k1 -= 1
            if k1 < 0:
                continue
            if (i1,j1) in max_obs and max_obs[(i1,j1)] >= k1:
                continue
            if (i1,j1) in max_obs:
                min_dist[(i1,j1)] = min_dist[(i,j)] + 1
            else:
                min_dist[(i1,j1)] = min(min_dist[(i,j)] + 1, min_dist[(i1,j1)])
            if (i1,j1) == (len(grid)-1,len(grid[0])-1):
                return min_dist[(i1,j1)]
            max_obs[(i1,j1)] = k1
            q.append((i1,j1,k1))
    return -1
        
print(shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 3))