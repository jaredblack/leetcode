def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    diff = sum(gas) - sum(cost)
    if diff < 0:
        return -1
    total = 0
    start_i = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            start_i = i + 1
            total = 0
    return start_i

        
print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))       
