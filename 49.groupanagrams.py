
from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for str in strs:
        groups[sorted(str)].append(str)
    return groups.values()

