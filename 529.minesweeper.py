# Topic exam (5/5)
def updateBoard(board: list[list[str]], click: list[int]) -> list[list[str]]:
    def in_bounds(i,j):
        return i >= 0 and i < len(board) and j >= 0 and j < len(board[0])

    def mine_count(i,j):
        mine_count = 0
        for k in range(i-1, i+2):
            for l in range(j-1, j+2):
                if in_bounds(k,l) and board[k][l] == 'M':
                    mine_count += 1
        return mine_count

    visited = set()
    def update_square(i,j):
        visited.add((i,j))
        mc = mine_count(i, j)
        if mc > 0:
            board[i][j] = str(mc)
        else:
            board[i][j] = 'B'
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if in_bounds(k,l) and (k,l) not in visited:
                        update_square(k,l)
    
    if board[click[0]][click[1]] == 'M':
        board[click[0]][click[1]] = 'X'
    else:
        update_square(*click)
            
    return board
