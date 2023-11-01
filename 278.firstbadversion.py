def isBadVersion(n):
    FIRST_BAD = 3
    if n >= FIRST_BAD:
        return True
    return False

def firstBadVersion(n: int) -> int:
    lo = 1
    hi = n
    mid1 = n // 2
    mid2 = mid1 + 1
    ver1 = isBadVersion(mid1)
    ver2 = isBadVersion(mid2)
    while not (not ver1 and ver2):
        if mid1 == 1 and ver1:
            return mid1
        if ver1:
            hi = mid1
        else:
            lo = mid2
        mid1 = (hi + lo) // 2
        mid2 = mid1 + 1
        ver1 = isBadVersion(mid1)
        ver2 = isBadVersion(mid2)
        
    return mid2

print(firstBadVersion(3))