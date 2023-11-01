# topic exam 5/5
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    # find row
    lo, hi = 0, len(matrix)
    row = None
    while hi > lo:
        mid = (hi + lo) // 2
        next_row_start = matrix[mid + 1][0] if mid + 1 < len(matrix) else 100000
        if matrix[mid][0] <= target < next_row_start:
            row = matrix[mid]
            break
        elif matrix[mid][0] <= target:
            lo = mid + 1
        else:
            hi = mid
    if row is None:
        return False
    lo, hi = 0, len(row)
    while hi - lo >= 1:
        mid = (hi + lo) // 2
        if target == row[mid]:
            return True
        elif target > row[mid]:
            lo = mid + 1
        else:
            hi = mid
    return False
    

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))