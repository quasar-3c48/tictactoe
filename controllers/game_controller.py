from models.board import board_full, free_cells
from models.game_state import GameState
from models.rules import check_winner, is_valid_move
from models.strategy_computer import pick_random_move
from models.symbols import is_allowed, opposite


class GameController:
    def __init__(self, board_size, win_length): #for the future view
        self.state = GameState(board_size, win_length)

    def start_game(self, player_symbol):
        if not is_allowed(player_symbol):
            return False
        self.state.player_symbol = player_symbol
        self.state.computer_symbol = opposite(player_symbol)
        self.state.reset_board()
        return True
    def snapshot(self): #we'll use it in the view
        return self.state
    def restart(self): #helper for the view too
        if not self.state.player_symbol:
            return False
        self.state.reset_board()
        return True

    def player_move(self, row, col): #for the view
        if self.state.status != "IN_PROGRESS":
            return
        if not is_valid_move(self.state.board, row, col):
            return
        self.apply_move(row, col, self.state.player_symbol)
        if self.state.status == "IN_PROGRESS":
            self.play_computer_turn()
    def play_computer_turn(self): # internal
        cell = pick_random_move(free_cells(self.state.board))
        if cell:
            self.apply_move(cell[0], cell[1], self.state.computer_symbol)
    def apply_move(self, row, col, symbol): #internal
        self.state.board[row][col] = symbol
        if check_winner(self.state.board, symbol, self.state.win_length):
            self.state.status = "WON"
            self.state.winner = symbol
        elif board_full(self.state.board):
            self.state.status = "DRAW"