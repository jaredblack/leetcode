def longestPalindrome(s: str) -> str:
    def find_pal(p1, p2):
        while p1 >= 0 and p2 < len(s):
            if s[p1] != s[p2]:
                return s[p1 + 1:p2]
            p1 -= 1
            p2 += 1
        return s[p1+1:p2]
    max_pal = ''
    for i, c in enumerate(s):
        # check odd case
        odd = find_pal(i, i)
        # check even case
        if i < len(s) - 1:
            even = find_pal(i, i+1)
        if len(odd) > len(max_pal):
            max_pal = odd
        if len(even) > len(max_pal):
            max_pal = even
    return max_pal

print(longestPalindrome("ac"))