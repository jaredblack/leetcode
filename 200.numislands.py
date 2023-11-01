def numIslands(grid: list[list[str]]) -> int:
    def in_bounds(i, j):
        return not (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]))
    
    def sink(i, j):
        if not in_bounds(i, j) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        sink(i+1, j)
        sink(i-1, j)
        sink(i, j-1)
        sink(i, j+1)
    
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '1':
                sink(i, j)
                islands += 1
    return islands

print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))