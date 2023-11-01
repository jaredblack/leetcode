def isIsomorphic(s: str, t: str) -> bool:
    cipher = {}
    for i, c in enumerate(s):
        if c not in cipher:
            if t[i] not in cipher.values():
                cipher[c] = t[i]
            else:
                return False
        elif cipher[c] != t[i]:
            return False
    return True

print(isIsomorphic("badc", "baba"))