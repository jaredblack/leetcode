from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    return [n for n, freq in Counter(nums).most_common(k)]


print(topKFrequent([1], 1)) 