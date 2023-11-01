from string import ascii_lowercase


def maximumCostSubstring(s: str, chars: str, vals: list[int]) -> int:
    char_vals = {c: ord(c) - 96 for c in ascii_lowercase}
    for i, char in enumerate(chars):
        char_vals[char] = vals[i]
    
    running = 0
    max_cost = 0
    for c in s:
        running += char_vals[c]
        if running < 0:
            running = 0
        elif running > max_cost:
            max_cost = running
    return max_cost

print(maximumCostSubstring("adaa", "d", [-1000]))