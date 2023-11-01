# this is like max sum subarray, but instead of resetting at the current element when we get below 0,
# we should consider either a) continuing with the current subarray, b) starting at the element where the current min subsequence starts (if the number
# we just got to is positive, that will probably make the min the max), or
# c) resetting at the current index

def maxProduct(nums: list[int]) -> int:
    curr_max = nums[0]
    overall_max = nums[0]
    curr_min = nums[0]
    for n in nums[1:]:
        candidates = (n, curr_max * n, curr_min * n)
        curr_max = max(candidates)
        curr_min = min(candidates)
        if curr_max > overall_max:
            overall_max = curr_max
    return overall_max
    
    

print(maxProduct([2,3,-2,4]))