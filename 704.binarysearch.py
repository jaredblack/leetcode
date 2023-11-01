def search(nums: list[int], target: int) -> int:
    lo, hi= 0, len(nums)
    while hi - lo >= 1:
        mid = (hi + lo) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid
    return -1

print(search([-1,0,3,5,9,12], 9))