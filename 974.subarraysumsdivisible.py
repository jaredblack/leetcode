# prefix sum
# this is a strange/difficult problem. the trick is realizing that 
# prefix[i] % k == prefix[j] % k when the subarray from i to j is divisible
# by k
from collections import defaultdict
import math

def subarraysDivByK(nums: list[int], k: int) -> int:
    prefix = [nums[0]]
    for n in nums:
        prefix.append(n + prefix[-1])
    
    mod_dict = defaultdict(int)
    for n in prefix:
        mod_dict[n % k] += 1

    subarrays = 0
    for mod in mod_dict.values():
        subarrays += math.comb(mod, 2)

    return subarrays

print(subarraysDivByK([4,5,0,-2,-3,1], 5))