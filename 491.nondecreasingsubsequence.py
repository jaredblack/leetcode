def findSubsequences(nums: list[int]) -> list[list[int]]:
    sequences = set()
    for i, n in enumerate(nums):
        curr_subseqs = {(n,)}
        for j in range(i + 1, len(nums)):
            if nums[j] >= n:
                sets_to_add = set()
                for s in curr_subseqs:
                    if s[-1] <= nums[j]:
                        sets_to_add.add(s + (nums[j],))
                curr_subseqs.update(sets_to_add)
        for sub in curr_subseqs:
            if len(sub) > 1:
                sequences.add(sub)
    return sequences

print(findSubsequences([4,6,7,7]))