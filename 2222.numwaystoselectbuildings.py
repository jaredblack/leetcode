def numberOfWays(s: str) -> int:
    ct0 = 0
    ct1 = 0

    p01 = 0
    p10 = 0
    p101 = 0
    p010 = 0
    for c in s:
        if c == '0':
            p10 += ct1
            p010 += p01
            ct0 += 1
        else:
            p01 += ct0
            p101 += p10
            ct1 += 1
    return p101 + p010