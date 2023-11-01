# 

from collections import Counter

def isValidSudoku(board: list[list[str]]) -> bool:
    def check_rows():
        for row in board:
            mc = Counter(row).most_common(2)
            if len(mc) > 1 and mc[1][1] > 1:
                return False
        return True

    def check_cols():
        for j in range(len(board[0])):
            count = Counter()
            for i in range(len(board)):
                count.update(board[i][j])
            mc = count.most_common(2)
            if len(mc) > 1 and mc[1][1] > 1:
                return False
        return True

    def check_squares():
        for sq_i in range(0, len(board), 3):
            for sq_j in range(0, len(board[0]), 3):
                count = Counter()
                for i in range(sq_i, sq_i + 3):
                    for j in range(sq_j, sq_j + 3):
                        count.update(board[i][j])
                mc = count.most_common(2)
                if len(mc) > 1 and mc[1][1] > 1:   
                    return False
        return True

    return check_rows() and check_cols() and check_squares()

print(isValidSudoku([[".","4",".",".",".",".",".",".","."],
                     [".",".","4",".",".",".",".",".","."],
                     [".",".",".","1",".",".","7",".","."],
                     [".",".",".",".",".",".",".",".","."],
                     [".",".",".","3",".",".",".","6","."],
                     [".",".",".",".",".","6",".","9","."],
                     [".",".",".",".","1",".",".",".","."],
                     [".",".",".",".",".",".","2",".","."],
                     [".",".",".","8",".",".",".",".","."]]))