def addToArrayForm(self, num: list[int], k: int) -> list[int]:
    n = list(''.join(map(int, num)))
    n += k
    return [int(d) for d in str(n)]