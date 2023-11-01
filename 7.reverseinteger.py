def reverse(x: int) -> int:
    neg = True if x < 0 else False
    if x == 0:
        return 0
    dstring = str(x)
    offset = 1 if neg else 0
    dlist = dstring[offset:]
    flist = []
    for c in reversed(dlist):
        flist.append(c)
    dstring = ''.join(map(str, flist))
    dint = -1 * int(dstring) if neg else int(dstring)
    return dint if -2**31 <= x <= 2**31-1 else 0


print(reverse(-123))
