def findMin(nums: list[int]) -> int:
    # find rotation point
    l, r = 0, len(nums)-1
    res = nums[0]
    while l <= r:
        mid = (l + r) // 2
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        res = min(res, nums[mid])
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
    return res
    
print(findMin([5,1,2,3,4]))