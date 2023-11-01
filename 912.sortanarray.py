# merge sort
from collections import Counter

# counting sort
def sortArray(nums: list[int]) -> list[int]:
    max_val = max(nums)
    min_val = min(nums)
    counter = Counter(nums)
    i = 0
    for n in range(min_val, max_val + 1):
        if n in counter:
            for j in range(i, counter[n] + i):
                nums[j] = n
            i += counter[n]
    return nums

# quicksort as it is hazily remembered from 235 4 years ago
# and from a quick review video i just watched
# tle :( though i think this is a reasonable quicksort implementation
def sortArray2(nums: list[int]) -> list[int]:
    def swap(i,j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def median_index(i,j,k):
        if nums[i] <= nums[j] <= nums[k] or nums[k] <= nums[j] <= nums[i]:
            return j
        if nums[j] <= nums[k] <= nums[i] or nums[i] <= nums[k] <= nums[j]:
            return k
        return i

    def quicksort(lo,hi):
        if hi - lo < 1:
            return
        piv_i = median_index(lo, ((hi - lo) // 2 + lo), hi)
        piv = nums[piv_i]
        swap(piv_i, hi)
        i = lo - 1
        for j in range(lo, hi):
            if nums[j] <= piv:
                i += 1
                (nums[i], nums[j]) = (nums[j], nums[i])
        piv_i = i+1
        swap(i+1, hi)
        quicksort(lo, piv_i-1)
        quicksort(piv_i + 1, hi)
    quicksort(0, len(nums) - 1)

nums = [3,4,1,4]
print(sortArray(nums))