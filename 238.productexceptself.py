from itertools import accumulate
from operator import mul

def productExceptSelf(nums: list[int]) -> list[int]:
    
    preprod_forw = list(accumulate(nums, mul))
    preprod_back = list(accumulate(nums[::-1], mul))[::-1]

    result = []

    for i in range(len(nums)):
        forw = preprod_forw[i - 1] if i > 0 else 1
        back = preprod_back[i + 1] if i < len(nums) - 1 else 1
        result.append(forw * back)
    return result

    
print(productExceptSelf([1,2,3,4]))