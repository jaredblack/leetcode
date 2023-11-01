def canJump(nums: list[int]) -> bool:
    reachable = [False for _ in range(len(nums))]
    reachable[0] = True
    for i, n in enumerate(nums):
        if reachable[i]:
            if nums[i] + i >= len(nums) - 1:
                return True
            for j in range(i+1, i+1+n):
                if j >= len(nums): break
                reachable[j] = True
    return reachable[-1]
