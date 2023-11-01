def generate(numRows: int) -> list[list[int]]:
    rows = [[1]]
    for i in range(1, numRows):
        last_row = rows[-1]
        row = [1]
        for j in range(len(rows[-1])-1):
            row.append(last_row[j] + last_row[j+1])
        row.append(1)
        rows.append(row)
    return rows
        
