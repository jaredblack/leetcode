def getRow(rowIndex: int) -> list[int]:
    prev_row = [1]
    row = [1]
    for _ in range(1, rowIndex+1):
        row = [1]
        for j in range(len(prev_row)-1):
            row.append(prev_row[j] + prev_row[j+1])
        row.append(1)
        prev_row = row
    return row