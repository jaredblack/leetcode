# first hard completed!
from collections import defaultdict
import heapq


def longestPath(parent: list[int], s: str) -> int:
    tree = defaultdict(list)
    for i, node in enumerate(parent):
        tree[node].append(i)

    longest_path = 0
    def find_longest_path(node):
        nonlocal longest_path
        child_lens = []
        for child in tree[node]:
            child_len = find_longest_path(child)
            if s[node] == s[child]:
                child_len = 0
            child_lens.append(child_len)
        top_two = heapq.nlargest(2, child_lens) if len(child_lens) >= 2 else child_lens
        if len(top_two) == 0:
            top_two = [0]
        if sum(top_two) + 1 > longest_path:
            longest_path = sum(top_two) + 1
        return top_two[0] + 1
    find_longest_path(0)
    return longest_path

print(longestPath([-1,0,0,1,1,2], 'abacbe'))