def addBinary(a: str, b: str) -> str:
    aint = int(a, 2)
    bint = int(b, 2)
    s = aint + bint
    return bin(s)[2:]