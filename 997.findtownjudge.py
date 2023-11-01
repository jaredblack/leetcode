# my own terminology was my own downfall
def findJudge(n: int, trust: list[list[int]]) -> int:
    # truster -> trusted
    truster_lists = [set() for _ in range(n)]
    # trusted -> truster
    trusted_lists = [set() for _ in range(n)]

    for pair in trust:
        truster_lists[pair[0] - 1].add(pair[1])
        trusted_lists[pair[1] - 1].add(pair[0])
    
    judge = -1
    for trusted, truster in enumerate(trusted_lists):
        if len(truster) == n - 1:
            judge = trusted
    if judge > -1:
        if len(truster_lists[judge]) != 0:
            judge = -1
        else:
            judge += 1
    return judge

print(findJudge(2, [[1,2]]))