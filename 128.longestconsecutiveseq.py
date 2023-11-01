# put all numbers in a set
# check if each num is a starting num (doesn't have one to the left in the set)
# if it is a starting num, start checking to the right and increment sequence length
# return the max seq
def longestConsecutive(nums: list[int]) -> int:
    nset = set(nums)
    m = -1000000
    for n in nums:
        if n-1 not in nset:
            l = 1
            while n+1 in nset:
                l += 1
                n += 1
            if l > m:
                m = l
    return m if m != -1000000 else 0   