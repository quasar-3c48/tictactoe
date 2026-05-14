"""Here, a rule to check if a move is a valid move. Just testing bounds and emptiness of cells"""
def is_valid_move(board, row, col):
    size = len(board)
    if not (0 <= row < size):
        return False
    if not (0 <= col < size):
        return False
    if board[row][col] != "":
        return False
    return True
"""Here checking a winner state or no"""
def lines_from_board(board):
    size = len(board)
    lines = []
    for a in range(size):
        lines.append(board[a])
    for b in range(size) :
        lines.append([board[r][b] for r in range(size)])

    for c in range(-size + 1, size):
        diag = [board[r][r - c] for r in range(size) if 0 <= r - c < size]
        lines.append(diag)

    for d in range(2 * size - 1) :
        diag = [board[r][d - r] for r in range(size) if 0 <= d - r < size]
        lines.append(diag)
    return lines
def check_winner(board, symbol, win_length):
    target = symbol * win_length
    for line in lines_from_board(board):
        if target in "".join(line):
            return True
            
    return False