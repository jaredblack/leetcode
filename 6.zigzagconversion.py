def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    rows = [[] for _ in range(numRows)]
    step = 1
    ind = 0
    for c in s:
        rows[ind].append(c)
        ind += step
        if ind == 0 or ind == numRows - 1:
            step *= -1
    return ''.join([''.join(row) for row in rows])

print(convert("PAYPALISHIRING", 3))