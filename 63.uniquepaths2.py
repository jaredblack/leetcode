def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    m,n = len(obstacleGrid), len(obstacleGrid[0])
    if obstacleGrid[-1][-1] == 1: return 0
    paths = [[0 for _ in range(n)] for _ in range(m)]
    for j, entry in enumerate(paths[0]):
        if obstacleGrid[0][j] > 0:
            break
        paths[0][j] = 1
    for i, row in enumerate(paths):
        if obstacleGrid[i][0] > 0:
            break
        row[0] = 1
    for i in range(1, m):
        for j in range(1, n):
            paths[i][j] = (paths[i-1][j] if obstacleGrid[i-1][j] == 0 else 0) + (paths[i][j-1] if obstacleGrid[i][j-1] == 0 else 0)
    return paths[m-1][n-1]

print(uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))