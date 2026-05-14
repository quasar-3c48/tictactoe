import tkinter as tk
class TkinterView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("tic tac toe")
        self.status = tk.StringVar(value="Choose your symbol to start.")
        self.buttons = []

        top = tk.Frame(self.root)
        top.pack(pady=8)
        tk.Button(top, text="Play as X", command=lambda: self.start("X")).pack(side=tk.LEFT, padx=4)
        tk.Button(top, text="Play as O", command=lambda: self.start("O")).pack(side=tk.LEFT, padx=4)
        tk.Button(top, text="Replay", command=self.replay).pack(side=tk.LEFT, padx=8)
        tk.Label(self.root, textvariable=self.status).pack(pady=4)

        state = self.controller.snapshot()
        board = tk.Frame(self.root)
        board.pack(pady=4)
        for r in range(state.board_size):
            row = []
            for c in range(state.board_size):
                btn = tk.Button(board, text=" ", width=10, height=4, font=("", 30, ""), command=lambda rr=r, cc=c: self.play(rr, cc))
                btn.grid(row=r, column=c, padx=3, pady=3)
                row.append(btn)
            self.buttons.append(row)
        self.render()

    def start(self, symbol):
        if self.controller.start_game(symbol):
            self.render()

    def replay(self):
        if self.controller.restart():
            self.render()
    def play(self, row, col):
        self.controller.player_move(row, col)
        self.render()
    def render(self):
        state = self.controller.snapshot()
        can_play = state.status == "IN_PROGRESS"
        for r, row in enumerate(state.board):
            for c, value in enumerate(row):
                mode = tk.NORMAL if can_play and value == "" else tk.DISABLED
                self.buttons[r][c].config(text=value if value else " ", state=mode)
        if state.status == "NOT_STARTED":
            self.status.set("Choose your symbol to start.")
        elif state.status == "IN_PROGRESS":
            self.status.set(f"You: {state.player_symbol} | Computer: {state.computer_symbol}")
        elif state.status == "DRAW":
            self.status.set("Draw. Click Replay.")
        elif state.winner == state.player_symbol:
            self.status.set("You win! Click Replay.")
        else:
            self.status.set("Computer wins. Click Replay.")