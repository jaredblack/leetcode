from collections import defaultdict
import heapq


def maximumSum(nums: list[int]) -> int:
    def digit_sum(n):
        s = 0
        for digit in str(n):
            s += int(digit)
        return s
    
    dsums = defaultdict(list)
    for n in nums:
        ds = digit_sum(n)
        heapq.heappush(dsums[ds], -n)
    
    curr_max = -1
    for nlist in dsums.values():
        if len(nlist) < 2:
            continue
        n1, n2 = -heapq.heappop(nlist), -heapq.heappop(nlist)
        if n1 + n2 > curr_max:
            curr_max = n1 + n2

    return curr_max

print(maximumSum([18,43,36,13,7]))