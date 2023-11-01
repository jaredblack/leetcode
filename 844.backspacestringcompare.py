# Slow version
def backspaceCompare(s: str, t: str) -> bool:
    strbuild = []
    for c in s:
        if c == '#':
            if len(strbuild):
                strbuild.pop()
        else:
            strbuild.append(c)
    sfinal = ''.join(strbuild)
    strbuild = []
    for c in t:
        if c == '#':
            if len(strbuild):
                strbuild.pop()
        else:
            strbuild.append(c)
    tfinal = ''.join(strbuild)
    return sfinal == tfinal


# Fast version
def backspaceCompareFast(s: str, t: str) -> bool:
    def build_reversed_str(s):
        strlist = []
        skip = 0
        for c in reversed(s):
            if c == '#':
                skip += 1
            elif skip:
                skip -= 1
            else: 
                strlist.append(c)
        return strlist
    return build_reversed_str(s) == build_reversed_str(t)
            
print(backspaceCompareFast("y#fo##f", "y#f#o##f"))