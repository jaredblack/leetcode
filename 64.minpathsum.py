import math


def minPathSum(grid: list[list[int]]) -> int:
    result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    result[0][0] = grid[0][0]
    for i, row in enumerate(result):
        for j, entry in enumerate(row):
            if (i, j) == (0,0): continue
            up = result[i-1][j] if i > 0 else math.inf
            left = result[i][j-1] if j > 0 else math.inf
            result[i][j] = min(up, left) + grid[i][j]
    return result[-1][-1]