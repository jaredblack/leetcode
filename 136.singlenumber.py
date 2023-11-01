from collections import Counter


def singleNumber(nums: list[int]) -> int:
    count = Counter(nums)
    
    for item in count:
        if count[item] != 2:
            return item

print(singleNumber([4,1,2,1,2]))