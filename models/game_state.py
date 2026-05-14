from models.board import new_board 

#i manage The game state. either for initialisation, either for restting the board state
class GameState:
    def __init__(self, board_size, win_length):
        if win_length > board_size:
            raise ValueError("Nope, A winning threshold length cannot be greater than the board size")
        if board_size < 3 or win_length < 3:
            raise ValueError("board_size and win_length must be >= 3")
        self.board_size, self.win_length = board_size, win_length
        self.board = new_board(board_size)
        self.player_symbol, self.computer_symbol, self.winner = None, None, None
        self.turn = "PLAYER"
        self.status = "NOT_STARTED"

    def reset_board(self): #for board reset upon game ending
        self.board, self.turn, self.status, self.winner = new_board(self.board_size), "PLAYER", "IN_PROGRESS", None