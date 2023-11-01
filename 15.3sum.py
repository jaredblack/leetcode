from collections import defaultdict

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    sols = set()
    for i in range(len(nums) - 2):
        start = nums[i]
        target = -start
        p1 = i + 1
        p2 = len(nums) - 1
        s = nums[p1] + nums[p2]
        while p1 < p2:
            if s == target:
                sols.append((start, nums[p1], nums[p2]))
            if s <= target:
                p1 += 1
            elif s >= target:
                p2 -= 1
            s = nums[p1] + nums[p2]
    return sols




# I thought I could sneak in within the constraints on an n^2 solution. 
# But then, they got me with the fact that multiple pairs in the array
# can add up to the same value which means if they stack them up on the 
# same entry in my dictionary we can get more of an n^3 runtime :(
def threeSum2(nums: list[int]) -> list[list[int]]:
    d = defaultdict(list)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                d[nums[i] + nums[j]].append((i, j))
    sols = set()
    for i, num in enumerate(nums):
        if -num in d:
            for entry in d[-num]:
                if i not in entry:
                    triple = tuple(sorted([nums[entry[0]], nums[entry[1]], num]))
                    sols.add(triple)
    return sols

print(threeSum([3,0,-2,-1,1,2]))