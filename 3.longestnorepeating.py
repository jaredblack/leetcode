def lengthOfLongestSubstring(s: str) -> int:
    def to_ind(c):
        return ord(c)
    
    if len(s) == 0:
        return 0

    last_occ = [0 for _ in range(128)]
    charset = set()
    start_i = 0
    max_len = 0
    for i, c in enumerate(s):
        if c in charset:
            if i - start_i > max_len:
                max_len = i - start_i
            if last_occ[ord(c)] + 1 > start_i:
                start_i = last_occ[to_ind(c)] + 1
        last_occ[to_ind(c)] = i
        charset.add(c)
    if len(s) - start_i > max_len:
        max_len = len(s) - start_i
    return max_len

print(lengthOfLongestSubstring("abba"))