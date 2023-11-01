def countOdds(low: int, high: int) -> int:
    diff = high - low
    base = diff // 2
    if low % 2 == 1 or high % 2 == 1:
        base += 1
    return base