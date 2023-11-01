def isSubsequence(s: str, t: str) -> bool:
    s_ind = 0
    if len(s) == 0:
        return True
    for c in t:
        if c == s[s_ind]:
            s_ind += 1
        if s_ind == len(s):
            return True
    return False


print(isSubsequence("b", "abc"))
