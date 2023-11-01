def uniquePaths(m: int, n: int) -> int:
    paths = [[0 for _ in range(n)] for _ in range(m)]
    paths[0] = [1 for _ in range(n)]
    for row in paths:
        row[0] = 1
    for i in range(1, n):
        for j in range(1, m):
            paths[i][j] = paths[i-1][j] + paths[i][j-1]
    return paths[m-1][n-1]