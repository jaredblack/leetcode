from collections import defaultdict
# Topic exam 4/5
# new approach: neetcode
# start at the ocean borders and perform DFS, having a shared visited
# set for each of the traversals from each set
# starting from the ocean edges is what avoids the recomputation
def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    def in_bounds(i,j):
        return i >= 0 and i < len(heights) and j >= 0 and j < len(heights[0])

    def dfs(i, j, possible):
        possible.add((i, j))
        for k, l in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if in_bounds(k,l) and (k, l) not in possible and heights[k][l] >= heights[i][j]:
                dfs(k, l, possible)

    possible_pacific = set()
    for i in range(len(heights)):
        dfs(i, 0, possible_pacific)
    for j in range(len(heights[0])):
        dfs(0, j, possible_pacific)

    possible_atlantic = set()
    for i in range(len(heights)):
        dfs(i, len(heights[0])-1, possible_atlantic)
    for j in range(len(heights[0])):
        dfs(len(heights)-1, j, possible_atlantic)

    return possible_pacific.intersection(possible_atlantic)

# TLE solution :( (from me)
def pacificAtlantic2(heights: list[list[int]]) -> list[list[int]]:
    NO = 0
    PAC = 1
    ATL = 2

    def get_curr_ocean(i, j):
        if i < 0 or j < 0:
            return PAC
        if i >= len(heights) or j >= len(heights[0]):
            return ATL
        return NO
    oceans_reachable = defaultdict(lambda: [0, 0])

    def dfs(i, j, starting, visited):
        visited.add((i, j))
        curr_ocean = get_curr_ocean(i, j)
        if curr_ocean:
            oceans_reachable[starting][curr_ocean-1] = 1
            return
        for k, l in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if (k, l) not in visited and (get_curr_ocean(k, l) or heights[k][l] <= heights[i][j]):
                dfs(k, l, starting, visited)
        visited.remove((i, j))

    for i in range(len(heights)):
        for j in range(len(heights[0])):
            dfs(i, j, (i, j), set())
    good1s = []
    for coord, ocean_pair in oceans_reachable.items():
        if ocean_pair == [1, 1]:
            good1s.append(coord)
    return good1s


print(pacificAtlantic([[1, 2, 2, 3, 5],
                       [3, 2, 3, 4, 4],
                       [2, 4, 5, 3, 1],
                       [6, 7, 1, 4, 5],
                       [5, 1, 1, 2, 4]]))
