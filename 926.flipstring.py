from collections import Counter
import math

def minFlipsMonoIncr(s: str) -> int:
    l0s = 0
    l1s = 0
    count = Counter(s)
    r0s = count['0']
    r1s = count['1']
    min_flips = math.inf
    for c in s:
        flips = min(l1s + r0s, l1s + r1s, l0s + r0s)
        if flips < min_flips:
            min_flips = flips
        if c == '0':
            l0s += 1
            r0s -= 1
        else:
            l1s += 1
            r1s -= 1
    return min_flips
    
print(minFlipsMonoIncr('010110'))