from collections import defaultdict


def distance(nums: list[int]) -> list[int]:
    equal_indices = defaultdict(list)
    for i, n in enumerate(nums):
        equal_indices[n].append(i)
    result = [0 for _ in range(len(nums))]
    for ilist in equal_indices.values():
        if len(ilist) < 2: continue
        result[ilist[0]] = sum(ilist) - len(ilist) * ilist[0]
        prev_i = ilist[0]
        for other_i, i in enumerate(ilist[1:]):
            other_i += 1
            diff = i - prev_i
            result[i] = result[prev_i] + diff * other_i - diff * (len(ilist) - other_i)
            prev_i = i
    return result

print(distance([0,5,3,1,2,8,6,6,6]))