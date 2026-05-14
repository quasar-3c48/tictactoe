"""Here, I've put helper functions to build the board, new_board for a new board init, free_cell to get the free cells of a specific board and board_full a boolean funton for empty board check"""
def new_board(size):
    new_board = []
    for i in range(size):
        sub_new_board = []
        for j in range(size):
            sub_new_board.append("")
        new_board.append(sub_new_board)
    return new_board

def free_cells(board):
    cells = []
    for r, row in enumerate(board):
        for c, value in enumerate(row):
            if value == "":
                cells.append((r, c))
    return cells

def board_full(board):
    return len(free_cells(board)) == 0