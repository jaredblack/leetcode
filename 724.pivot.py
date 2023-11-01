def pivotIndex(nums: list[int]) -> int:
    prefix = []
    for i, n in enumerate(nums):
        if i != 0:
            prefix.append(n + prefix[i-1])
        else:
            prefix.append(n)
    
    for i, n in enumerate(prefix):
        if i == 0 and n == prefix[-1]:
            return i
        elif i != 0 and prefix[i-1] == (prefix[-1] - nums[i]) / 2:
            return i
    return -1

print(pivotIndex([-1,-1,0,1,1,1]))