def minCostClimbingStairs(cost: list[int]) -> int:
    best_step = [cost[0], cost[1]]
    for i in range(2, len(cost)):
        best_step.append(min(best_step[i-1], best_step[i-2]) + cost[i])
    return min(cost[-2:])