# Cracking the Coding Interview 1.2

# my solution O(nlogn)
def isAnagram(s: str, t: str) -> bool:
    s_list = sorted(list(s))
    t_list = sorted(list(t))
    return s_list == t_list
    
from collections import Counter
# Adapted book solution. LeetCode runtime is similar. I *think* this should be O(n + m), where n is len(s)
# and m is len(t), so I think it's analytically faster.
def isAnagramCounter(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counter = Counter(s)
    for c in t:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True