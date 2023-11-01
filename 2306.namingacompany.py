from collections import defaultdict
import itertools


def distinctNames(ideas: list[str]) -> int:
    ideas_dict = defaultdict(set)
    for idea in ideas:
        ideas_dict[idea[0]].add(idea[1:])
    tot = 0
    for i1, i2 in itertools.combinations(ideas_dict.keys(), 2):
        intersect_len = len(ideas_dict[i1].intersection(ideas_dict[i2]))
        tot += 2 * (len(ideas_dict[i1]) - intersect_len) * (len(ideas_dict[i2]) - intersect_len)
    return tot

print(distinctNames(["aaa","baa","caa","bbb","cbb","dbb"]))